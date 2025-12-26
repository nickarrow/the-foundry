---
name: Barille Black
xp_spent: 0
xp_added: 0
momentum: 2
edge: 1
heart: 3
iron: 2
shadow: 1
wits: 2
health: 5
spirit: 5
supply: 5
Quests_Progress: 0
Quests_XPEarned: 0
Bonds_Progress: 0
Bonds_XPEarned: 0
Discoveries_Progress: 0
Discoveries_XPEarned: 0
iron-vault-kind: character
assets:
  - id: asset:starforged/path/brawler
    abilities:
      - true
      - false
      - false
    controls: {}
    options: {}
  - id: asset:starforged/support_vehicle/snub_fighter
    abilities:
      - true
      - false
      - false
    controls:
      integrity: 4
      integrity/battered: false
      2/victory_marks: 0
    options:
      name: SF-27
  - id: asset:starforged/path/bounty_hunter
    abilities:
      - true
      - false
      - false
    controls: {}
    options: {}
initiative: false
---
![[barille black profile.png|center|100]] 
```iron-vault-character-meters
```
> [!assets]- ASSETS
> ```iron-vault-character-assets
> ```

> [!gear]- GEAR
> - A compact multitool capable of 'light' matter manipulation
> - Hand terminal
> - Kinetic pistol
> - A leather bound journal and pen
> - A coin of black iron, embossed with an insignia

> [!in-progress]- TRACKS IN-PROGRESS
> ```dataview
> TABLE WITHOUT ID file.link as "Vows"
> FROM #incomplete 
> WHERE track-type = "Vow"
> WHERE character = "Barille Black"
> SORT file.mtime DESC
> ```
> 
> ```dataview
> TABLE WITHOUT ID file.link as "Tracks"
> FROM #incomplete
> WHERE track-type != "Vow"
> WHERE track-type != "Connection"
> WHERE iron-vault-kind != "clock"
> WHERE character = "Barille Black"
> SORT file.mtime DESC
> ```

> [!bonds]- BONDS
> ```dataview
> TABLE WITHOUT ID file.link as "Bonds"
> WHERE track-type = "Connection"
> WHERE character = "Barille Black"
> SORT file.mtime DESC
> ```

> [!impacts]- IMPACTS
> ```iron-vault-character-impacts
> ```

> [!legacies]- LEGACIES
> ```iron-vault-character-special-tracks
> ```

> [!complete]- TRACKS COMPLETED
> ```dataview
> TABLE WITHOUT ID file.link as "Vows"
> FROM #complete
> WHERE track-type = "Vow"
> WHERE character = "Barille Black"
> SORT file.mtime DESC
> ```
> 
> ```dataview
> TABLE WITHOUT ID file.link as "Tracks"
> FROM #complete
> WHERE track-type != "Vow"
> WHERE track-type != "Connection"
> WHERE iron-vault-kind != "clock"
> WHERE character = "Barille Black"
> SORT file.mtime DESC
> ```