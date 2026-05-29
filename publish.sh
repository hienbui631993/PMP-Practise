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
   "$SRC/quiz.html" \
   "$SRC/qa_dataset.json" \
   "$SRC/principles.html" \
   "$SRC/principles_dataset.json" \
   "$SRC/README.md" \
   "$SRC/progress.md" \
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
