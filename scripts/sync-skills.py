#!/usr/bin/env python3
"""
sync-skills.py — Espejo VERDADERO de skills: .claude/skills/ → .agents/skills/.

Alcances gestionados aquí (replica, purga huérfanos y reporta):
  1. Raíz:    .claude/skills/                    → .agents/skills/     (guía + skills de marca)
  2. Studios: Content Manager/*/.claude/skills/  → su ./.agents/skills/ (ej. carousel-studio)

Excluido: "Content Manager/video-studio" — es un kit vendido (HyperFrames) que se
sincroniza a sí mismo con `npm run sync:skills` desde su propio directorio.
Nunca mezclar alcances.

Uso:
    python scripts/sync-skills.py          # sincroniza todos los alcances
    python scripts/sync-skills.py --check  # solo reporta diferencias (exit 1 si hay drift)
"""
import argparse
import filecmp
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXCLUDED_STUDIOS = {"video-studio"}


def find_scopes():
    """[(claude_skills_dir, agents_skills_dir), ...]"""
    scopes = [(ROOT / ".claude" / "skills", ROOT / ".agents" / "skills")]
    cm = ROOT / "Content Manager"
    if cm.is_dir():
        for studio in sorted(p for p in cm.iterdir() if p.is_dir()):
            claude = studio / ".claude" / "skills"
            if claude.is_dir() and studio.name not in EXCLUDED_STUDIOS:
                scopes.append((claude, studio / ".agents" / "skills"))
    return scopes


def diff_scope(claude_skills, agents_skills):
    """Return (copied, stale) for one scope."""
    copied, stale = [], []
    for src in sorted(p for p in claude_skills.rglob("*") if p.is_file()):
        dst = agents_skills / src.relative_to(claude_skills)
        if not dst.exists() or not filecmp.cmp(src, dst, shallow=False):
            copied.append(src)
    if agents_skills.is_dir():
        for dst in sorted(p for p in agents_skills.rglob("*") if p.is_file()):
            if not (claude_skills / dst.relative_to(agents_skills)).exists():
                stale.append(dst)
    return copied, stale


def prune(stale, agents_skills):
    """Delete orphan files; then empty orphan dirs (tolerate OneDrive locks)."""
    for f in stale:
        f.unlink(missing_ok=True)
    dirs = sorted({f.parent for f in stale}, key=lambda d: len(str(d)), reverse=True)
    for d in dirs:
        while d != agents_skills and d.is_dir() and d.exists() and not any(d.iterdir()):
            try:
                d.rmdir()
            except OSError as e:  # OneDrive/file-lock: empty dir is harmless
                print(f"  WARN could not remove empty orphan dir {d.name}: {e.strerror or e}")
                break
            d = d.parent


def main():
    parser = argparse.ArgumentParser(description="Sync skills .claude -> .agents (root + studios)")
    parser.add_argument("--check", action="store_true", help="report differences only")
    args = parser.parse_args()

    total_copied = total_stale = 0
    for claude_skills, agents_skills in find_scopes():
        if not claude_skills.is_dir():
            continue
        copied, stale = diff_scope(claude_skills, agents_skills)

        if args.check:
            for f in copied:
                print(f"DIFF   {claude_skills.name} -> {agents_skills.name} : {f.relative_to(claude_skills)}")
            for f in stale:
                print(f"STALE  orphan in .agents : {f.relative_to(agents_skills)}")
        else:
            if stale:
                prune(stale, agents_skills)
            agents_skills.mkdir(parents=True, exist_ok=True)
            for src in copied:
                dst = agents_skills / src.relative_to(claude_skills)
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)

        label = str(claude_skills.relative_to(ROOT)) or ".claude/skills"
        if args.check:
            scope_state = "in sync" if not (copied or stale) else \
                f"{len(copied)} file(s) need sync, {len(stale)} orphan(s)"
            print(f"  {label}: {scope_state}")
        else:
            state = f"synced {len(copied)}" + (f", pruned {len(stale)} orphan(s)" if stale else "") \
                if (copied or stale) else "already in sync"
            names = sorted(d.name for d in agents_skills.iterdir() if d.is_dir())
            print(f"  {label}: {state} ({len(names)} skills)")
        total_copied += len(copied)
        total_stale += len(stale)

    print(f"Scopes checked: {len(find_scopes())}")
    if args.check:
        sys.exit(1 if (total_copied or total_stale) else 0)


if __name__ == "__main__":
    main()
