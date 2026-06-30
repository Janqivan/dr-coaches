# Digital Rocket — Coach Packs (Plugin Marketplace)

A single Claude **plugin marketplace** bundling all of DR's synthetic operator-coach packs:
**31 advisor personas** across agency mechanics, conversion craft, B2B GTM, verticals, and operations.

Each coach is a slash command (e.g. `/negotiation-voss`, `/pricing-enns`, `/aimozi`) and also
auto-triggers on natural language ("what would Voss do", "audit my offer", etc.).

| Pack | Coaches | Focus |
|---|---|---|
| `agency-builder-pack` | 8 | Agency positioning/pricing + B2B GTM |
| `craft-builder-pack` | 9 | Copy/CRO/design + verticals + solo |
| `ultimate-coach-pack` | 13 | Negotiation, positioning, hiring, strategy, copy, ops |
| `aimozi` | 1 | Alex Hormozi business advisor |

Full roster with slash commands: see **COACH-INDEX.md**.
Install steps for your team: see **INSTALL.md**.

## Fastest path for the team (Cowork)
1. One person creates a GitHub repo from this folder and pushes it (run `./push-to-github.sh owner/repo`).
2. Each teammate: **Claude Desktop → Cowork tab → Customize → Plugins → "+" → Add marketplace →** paste the repo URL.
3. Install the four packs, refresh. Done.

> Want zero clicks for the team? An org admin can add these once under
> **Organization settings → Plugins** and push them to everyone. See INSTALL.md → "Route B".

## What's inside
```
dr-coach-packs/
├── .claude-plugin/marketplace.json   ← the catalog (lists all 4 packs)
├── agency-builder-pack/              ← each pack is a self-contained plugin
├── craft-builder-pack/
├── ultimate-coach-pack/
├── aimozi/
├── README.md
├── INSTALL.md
├── COACH-INDEX.md
└── push-to-github.sh
```

Maintainer: Ivan Janku / Digital Rocket — ivan@digitalrocketads.com

## Team enablement (read these)
- **QUICKSTART.md** — 1-page: install + your first coach by role.
- **COACHES.md** — the full playbook: router ("which coach when") + a card for all 31 coaches.
- **INSTALL.md** — every install route (Cowork, org-admin, CLI).
- **COACH-INDEX.md** — flat one-line index of all 31.

## Install granularity
This marketplace exposes **34 installable units: 4 packs + 30 individual coaches.** Install a full pack, or just the single coaches you want — each coach is self-contained and ships its own framework corpus.
