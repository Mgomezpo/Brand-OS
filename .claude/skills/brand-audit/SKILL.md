---
name: brand-audit
description: Run an evidence-based system audit of Brand OS. Verifies aspect ratio compliance (strict 3:4 for carousels, 9:16 for video), 96px safe margins, proof bank substantiation, zero broken wiki-links, anti-slop compliance, and placeholder elimination. Saves a dated report in audits/.
---

## What this skill does

Performs an exhaustive, 6-axis operational audit of the Brand OS workspace. Awards points exclusively for verified evidence rather than file existence. Automatically generates a dated Markdown audit report in `audits/YYYY-MM-DD-brand-audit.md`.

## The 6 Audit Checks

### 1. Placeholder Residue & Personalization Check
- Scans `vault/` and `design-system/` for unpopulated template strings like `{{NOMBRE_MARCA}}`, `{{NOMBRE_CREADOR}}`, `[Insertar]`, `[Your answer here]`.
- **Pass criterion:** 0 unpopulated placeholders. If found, lists the exact files and lines.

### 2. Aspect Ratio Compliance (The 3:4 & 9:16 Rule)
- Verifies that all carousel documentation, CSS tokens, and scripts enforce **3:4 (1080 × 1440 px)**.
- Flags any legacy 4:5 (1080 × 1350 px) or 1:1 square mentions.
- Verifies that video studio templates enforce **9:16 (1080 × 1920 px)**.
- **Pass criterion:** 100% adherence to 3:4 and 9:16.

### 3. Safe Margin & Design Tokens Integrity
- Verifies that `design-system/index.css` and slide templates respect the minimum **96px safe margin** on all edges.
- Validates that the 3-color rule is respected: `--surface-page` (background), `--text-strong` (reading typography), `--accent` (single focal highlight per slide).
- **Pass criterion:** Safe margins and token hierarchy verified in CSS and render templates.

### 4. Proof Bank Cross-Referencing (Anti-Hallucination)
- Inspects all drafts, templates, and batch files in `vault/` and `Content Manager/`.
- Extracts every statistic, dollar figure, multiplier, percentage, and case study claim.
- Cross-references each claim against `vault/Conceptos/proof_bank.md`.
- **Pass criterion:** Every metric cited has an explicit entry in `proof_bank.md`. Any ungrounded claim is flagged as a high-risk defect.

### 5. Obsidian Wiki-Link Resolution
- Parses all `[[wiki-links]]` across `vault/`.
- Resolves each link against the actual filesystem in `vault/`.
- **Pass criterion:** 0 broken wiki-links.

### 6. Tone of Voice & Anti-Slop Audit
- Checks drafts against the forbidden blacklist in `vault/Conceptos/tone_of_voice.md`.
- Flags generic AI phrasing (e.g., "adéntrate en", "en el vertiginoso mundo", "game-changer", "desbloquea tu potencial", "revolucionario").
- **Pass criterion:** 0 blacklisted words in active drafts.

---

## Output Report Structure

Every audit run must save a report to `audits/YYYY-MM-DD-brand-audit.md`:

```markdown
# Brand OS Audit Report — YYYY-MM-DD

- **Overall Score:** [0-100] / 100
- **Status:** [GREEN / YELLOW / RED]

## Summary of Findings
| Check | Status | Evidence / Notes |
|---|---|---|
| 1. Placeholders | PASS / FAIL | [Count of remaining placeholders] |
| 2. Ratios (3:4 & 9:16) | PASS / FAIL | [Adherence to 1080x1440 and 1080x1920] |
| 3. Safe Margins | PASS / FAIL | [96px padding verified in CSS] |
| 4. Proof Bank | PASS / FAIL | [Citations verified against proof_bank.md] |
| 5. Wiki Links | PASS / FAIL | [0 broken links out of total scanned] |
| 6. Anti-Slop | PASS / FAIL | [Blacklist violations detected] |

## Prioritized Action Items
1. [Highest priority fix with file link]
2. [Second priority fix]
3. [Third priority fix]
```
