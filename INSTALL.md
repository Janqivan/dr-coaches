# INSTALL — DR Coach Packs

This bundle is a **plugin marketplace**: one catalog (`.claude-plugin/marketplace.json`) that lists
four plugins. Pick the route that matches how your team runs Claude. **Route A is the default.**

Verified against Anthropic docs (code.claude.com/docs/en/plugin-marketplaces,
support.claude.com "Use plugins in Claude") — June 2026.

---

## ⚠️ Read this first
Google Drive is **storage/backup only** — Cowork cannot install a plugin marketplace from a Drive
folder or zip. Cowork adds a custom marketplace from a **GitHub repo URL** or an **org-admin upload**.
So the team installs from GitHub (Route A or B). The Drive zip is the offline backup / source of truth.

---

## Route A — Cowork via GitHub repo  ← recommended, per-user
**One-time setup (you, once):**
1. Create the repo + push. From inside this folder:
   ```bash
   ./push-to-github.sh Janqivan/dr-coaches
   ```
   (Needs the `gh` CLI, or it falls back to `git push` against a repo you've already created.)
   Manual equivalent:
   ```bash
   git init && git add -A && git commit -m "DR coach packs" && git branch -M main
   git remote add origin https://github.com/Janqivan/dr-coaches.git
   git push -u origin main
   ```

**Each teammate (≈30 seconds):**
1. Claude Desktop → **Cowork** tab → **Customize** (left sidebar) → **Plugins** tab.
2. Click **"+" → Add marketplace** → paste `https://github.com/Janqivan/dr-coaches`.
3. The four packs appear. Click **Install** on each (or just the ones they need).
4. Refresh / start a new session. Type `/` to confirm the coaches show up (e.g. `/aimozi`).

Private repo? Same steps — each teammate must have GitHub access to the repo.

---

## Route B — Org-admin marketplace  ← zero clicks for the team
Best if you want everyone to get the packs automatically.
1. Do the GitHub push from Route A (the org marketplace syncs from a repo).
2. **Organization settings → Plugins → Add** → point it at `Janqivan/dr-coaches`.
3. Add each of the four plugins and set the **installation preference** (auto-install).
4. Team members get the packs on their next session / plugin refresh — nothing for them to do.

---

## Route C — Claude Code (CLI), if anyone uses the terminal
```bash
# from a GitHub repo:
claude plugin marketplace add Janqivan/dr-coaches
claude plugin install agency-builder-pack@dr-coach-packs
claude plugin install craft-builder-pack@dr-coach-packs
claude plugin install ultimate-coach-pack@dr-coach-packs
claude plugin install aimozi@dr-coach-packs
```
Or inside an interactive session: `/plugin marketplace add Janqivan/dr-coaches` then `/plugin install <pack>@dr-coach-packs`.

---

## Route D — Local test / offline (CLI only)
Unzip `dr-coach-packs.zip`, then:
```bash
claude plugin marketplace add ./dr-coach-packs
claude plugin install ultimate-coach-pack@dr-coach-packs
```
(Local-path marketplaces are a CLI feature; Cowork does not support them reliably — use Route A.)

---

## Updating later
Edit a pack, **bump its `version`** in `<pack>/.claude-plugin/plugin.json`, then push to GitHub.
Existing users pull the change via **Customize → Plugins → ⟳ refresh** (Cowork) or
`claude plugin marketplace update` (CLI). If you don't bump `version`, existing installs keep the
cached copy and won't see the change.

## Validate before sharing (optional, needs Claude Code)
```bash
claude plugin validate .
```
Checks `marketplace.json` syntax, duplicate names, and each pack's `plugin.json`.

## Troubleshooting
- **"Marketplace not loading"** → confirm `.claude-plugin/marketplace.json` exists at the repo root and the repo is pushed.
- **Coaches don't appear after install** → start a new session / refresh plugins; type `/` and look for the pack-namespaced commands.
- **Private repo install fails** → confirm the teammate has GitHub access (`gh auth status`).

---

## Install a whole pack OR a single coach (new)
The marketplace lists **34 installable units: the 4 packs + 30 individual coaches.**
- **Whole pack** (all its coaches at once): install `agency-builder-pack`, `craft-builder-pack`, `ultimate-coach-pack`, or `aimozi`.
- **Single coach** (just that one — it carries its own framework corpus): install e.g. `negotiation-voss`, `pricing-enns`, `copy-wiebe`.

**Cowork:** after adding the marketplace (Customize → Plugins), you'll see all 34 — click Install on whatever you want.

**CLI:**
```
claude plugin install ultimate-coach-pack@dr-coach-packs   # the whole pack
claude plugin install negotiation-voss@dr-coach-packs      # just one coach
```
Tip: install the pack **or** its individual coaches, not both, or you'll get the same command twice (namespaced).
