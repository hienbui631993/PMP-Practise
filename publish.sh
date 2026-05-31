#!/usr/bin/env bash
# Publish the current PMP prep files to the claude-vibe repo under "pmp prep/".
# Usage:  bash publish.sh ["commit message"]
set -e

SRC="D:/Claude Code/PMP Practise"
REPO="D:/Claude Code/_clone_tmp"          # local clone of hienbui631993/claude-vibe
DST="$REPO/pmp prep"

msg="${1:-Update PMP prep ($(date '+%Y-%m-%d %H:%M'))}"

mkdir -p "$DST/.claude"

# Copy the files we publish (edit this list if you add/remove files)
cp "$SRC/index.html" \
   "$SRC/banks.html" \
   "$SRC/quiz.html" \
   "$SRC/qa_dataset.json" \
   "$SRC/principles.html" \
   "$SRC/principles_dataset.json" \
   "$SRC/dnd.html" \
   "$SRC/dnd_dataset.json" \
   "$SRC/100 pmp dnd.md" \
   "$SRC/eco.html" \
   "$SRC/exam.html" \
   "$SRC/processgroups.html" \
   "$SRC/processgroups_dataset.json" \
   "$SRC/Process Groups Practice Guide.md" \
   "$SRC/pmbok7guide.html" \
   "$SRC/pmbok7guide_dataset.json" \
   "$SRC/Project Management Body of Knowledge.md" \
   "$SRC/pmbok8guide.html" \
   "$SRC/pmbok8guide_dataset.json" \
   "$SRC/PMBOK Guide 8th Edition.md" \
   "$SRC/tools.html" \
   "$SRC/tools_dataset.json" \
   "$SRC/63 Project Management Tools Explained.md" \
   "$SRC/knowledgemap.html" \
   "$SRC/pmbok7.html" \
   "$SRC/pmbok7_dataset.json" \
   "$SRC/150 PMBOK 7 by David McLachlan.md" \
   "$SRC/dnd2.html" \
   "$SRC/dnd2_dataset.json" \
   "$SRC/110 DND by David McLachlan.md" \
   "$SRC/agile.html" \
   "$SRC/agile_dataset.json" \
   "$SRC/200 AGILE PMP.md" \
   "$SRC/waterfall.html" \
   "$SRC/waterfall_dataset.json" \
   "$SRC/100 Waterfall PMP Questions and Answers.md" \
   "$SRC/pmp-examination-content-outline.pdf" \
   "$SRC/README.md" \
   "$SRC/progress.md" \
   "$SRC/LIMITATIONS.md" \
   "$SRC/PROMTP.md" \
   "$SRC/200 untra hard transcript.md" \
   "$SRC/50 Principles.md" \
   "$SRC/transcript.html" \
   "$SRC/.gitignore" \
   "$DST/"
cp "$SRC/.claude/launch.json" "$DST/.claude/launch.json"

cd "$REPO"
git add -A
if git diff --cached --quiet; then
  echo "No changes to publish."
  exit 0
fi
git commit -m "$msg"
git push origin main
echo "Published: https://github.com/hienbui631993/claude-vibe/tree/main/pmp%20prep"
