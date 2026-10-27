#!/usr/bin/env python3
"""
sync-skills.py — Mirrorueba de skills de nivel raíz: .claude/skills/ → .agents/skills/.

Espejo VERDADERO: replica, elimina espejos huérfanos y reporta el estado.
Alcance: SOLO los skills de marca de nivel raíz (brand-onboard, brand-audit,
carousel-batch, script-shortform, grill-me, level-up).
Los skills técnicos del motor de video viven en
"Content Manager/video-studio/.claude/skills/" y se sincronizan allí con
"npm run sync:skills" (sync-codex-skills.mjs) — no mezclar alcances.

Uso:
    python scripts/sync-skills.py          # sincroniza
    python scripts/sync-skills.py --check  # solo reporta diferencias (exit 1 si hay)
"""
import argparse
import filecmp
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CLAUDE_SKILLS = ROOT / ".claude" / "skills"
AGENTS_SKILLS = ROOT / ".agents" / "skills"


def diff_status():
    """Return (copied_dirs, stale_dirs_and_files) comparing both trees."""
    if not CLAUDE_SKILLS.exists():
        print(f"Error: {CLAUDE_SKILLS} not found.")
        sys.exit(2)

    claude_files = sorted(p for p in CLAUDE_SKILLS.rglob("*") if p.is_file())
    copied, stale = [], []

    for src in claude_files:
        dst = AGENTS_SKILLS / src.relative_to(CLAUDE_SKILLS)
        if not dst.exists() or not filecmp.cmp(src, dst, shallow=False):
            copied.append(src)

    if AGENTS_SKILLS.exists():
        for dst in sorted(AGENTS_SKILLS.rglob("*")):
            src = CLAUDE_SKILLS / dst.relative_to(AGENTS_SKILLS)
            if not src.exists():
                stale.append(dst)

    return copied, stale


def main():
    parser = argparse.ArgumentParser(description="Sync root skills .claude -> .agents")
    parser.add_argument("--check", action="store_true", help="report differences only")
    args = parser.parse_args()

    copied, stale = diff_status()

    if args.check:
        for f in copied:
            print(f"DIFF  .claude -> .agents : {f.relative_to(CLAUDE_SKILLS)}")
        for f in stale:
            print(f"STALE orphan in .agents  : {f.relative_to(AGENTS_SKILLS)}")
        if copied or stale:
            print(f"\n{len(copied)} file(s) need sync, {len(stale)} orphan(s) to prune.")
            sys.exit(1)
        total = len([p for p in AGENTS_SKILLS.rglob('*') if p.is_file()])
        print(f"In sync ({total} mirrored files).")
        return

    if stale:
        for f in stale:
            print(f"prune orphan: {f.relative_to(AGENTS_SKILLS)}")
            f.unlink(missing_ok=True)
        for d in sorted({f.parent for f in stale}, reverse=True):
            while d != AGENTS_SKILLS and d.is_dir() and not any(d.iterdir()):
                d.rmdir()
                d = d.parent

    AGENTS_SKILLS.mkdir(parents=True, exist_ok=True)
    for src in copied:
        dst = AGENTS_SKILLS / src.relative_to(CLAUDE_SKILLS)
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)

    copied_dirs = sorted(d.name for d in AGENTS_SKILLS.iterdir() if d.is_dir())
    if copied:
        print(f"Synced {len(copied)} file(s):")
        for f in copied:
            print(f"  -> {f.relative_to(CLAUDE_SKILLS)}")
    else:
        print("Nothing to sync (already in sync).")
    print(f"Active skills ({len(copied_dirs)}): {', '.join(copied_dirs)}")


if __name__ == "__main__":
    main()
