#!/usr/bin/env python3
"""
Sync skills from .claude/skills/ to .agents/skills/ (or vice-versa).
Brand OS dual-agent compatibility maintenance script.
"""
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CLAUDE_SKILLS = ROOT / ".claude" / "skills"
AGENTS_SKILLS = ROOT / ".agents" / "skills"

def sync():
    if not CLAUDE_SKILLS.exists():
        print(f"Error: {CLAUDE_SKILLS} not found.")
        return

    AGENTS_SKILLS.mkdir(parents=True, exist_ok=True)
    shutil.copytree(CLAUDE_SKILLS, AGENTS_SKILLS, dirs_exist_ok=True)
    print(f"Successfully synced skills from {CLAUDE_SKILLS} to {AGENTS_SKILLS}")
    skills = [d.name for d in AGENTS_SKILLS.iterdir() if d.is_dir()]
    print(f"Active skills ({len(skills)}): {', '.join(skills)}")

if __name__ == "__main__":
    sync()
