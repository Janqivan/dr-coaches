#!/usr/bin/env bash
set -euo pipefail
# Usage: ./push-to-github.sh <owner/repo>
# Example: ./push-to-github.sh digitalrocket/dr-coach-packs
REPO="${1:?Pass owner/repo, e.g. digitalrocket/dr-coach-packs}"
git init -q
git add -A
git commit -qm "DR coach packs marketplace — 4 packs, 31 coaches" || true
git branch -M main
if command -v gh >/dev/null 2>&1; then
  gh repo create "$REPO" --private --source=. --remote=origin --push
else
  git remote add origin "https://github.com/$REPO.git" 2>/dev/null || git remote set-url origin "https://github.com/$REPO.git"
  git push -u origin main
fi
echo
echo "Pushed. Now in Cowork: Customize > Plugins > + > Add marketplace >"
echo "  https://github.com/$REPO"
