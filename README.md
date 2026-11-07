# Crusaders — Game
Crusaders is a 3D, free-for-all fighting game currently in beta and available on Roblox!

For those who wish to see the game's progress from before I added GitHub to my workflow, please refer to [The Timeline](https://github.com/altair5607249/Crusaders-Game-Timeline).

## Play the Game!
| Medium | Requirements | Compatibility | Status |
| --- | --- | --- | --- |
| Live Game | Roblox Account (Verified 16+) | PC & Mobile | [Active](https://www.roblox.com/games/123600574843310/Crusaders) |
| Source File | Roblox Account; Roblox Studio | PC | [Active](https://github.com/altair5607249/Crusaders-Game/blob/main/7046.rbxl)
| Unity | N/A | N/A | In Progress |

### Notes  
- I have not met Roblox's Highly-Engaged Player (HEP) threshold, so the live game will be age restricted to 16+ until then.
- Currently working to create a Unity version of the game.
- You need a Roblox account to play the game, whether via Roblox itself or Roblox Studio; it only takes a few minutes to make if you don't already have one!
  - If you decide to play the public release of the game (the first link), you must verify that you're of 16 years or older.
  - If you decide to open the binary place file (the second link), you must download Roblox Studio.

## Codebase
### Legend
- Connections
  - Solid Line — Relation
  - Solid Arrow — Require
  - Thick Arrow — Init
  - Dotted Arrow — Remote Event
- Colors
  - Blue — Client
  - Green — Server
  - Purple — Universal

### Combat Flow

### Initialization

### Full System Diagram
```mermaid
flowchart TB;

  classDef serverNode fill:#5bf547,stroke:#000000,color:#000000
  classDef clientNode fill:#42a1f5,stroke:#000000,color:#000000
  classDef universalNode fill:#b549eb,stroke:#000000,color:#000000

  ModuleLoader2==>Energy;
  ModuleLoader2==>KnockbackHandler;
  Energy==>M1_Client;
  Energy==>Sol_Client;
  Energy==>Movement;
  M1_Client-.->ModuleLoader;
  Sol_Client-.->ModuleLoader;
  Movement-.->MovementManager;
  ModuleLoader==>Administration;
  ModuleLoader==>Managers;
  ModuleLoader==>OutputModules;
  ModuleLoader==>Matter-->MapManager;

  subgraph Administration
    Commands;
    Permissions;
  end

  subgraph Managers
    CooldownManager;
    DamageManager;
    DataManager;
    KnockbackManager;
    MapManager;
    MovementManager;
    StunManager;
  end

  subgraph OutputModules
    M1_Server-->DamageManager;
    Bare_Server-->DamageManager;
    Weapon_Server-->DamageManager;
  end

  KnockbackManager-->Space;
  DamageManager-->Space;
  DamageManager-->DataManager;
  DamageManager-->KnockbackManager;
  DamageManager-->StunManager;
  M1_Server-->Time;
  Bare_Server-->Time;
  Weapon_Server-->Time;
  StunManager-->Time;
  M1_Server-->Space;
  Bare_Server-->Space;
  Weapon_Server-->Space;
  KnockbackManager-.->ModuleLoader2-->KnockbackHandler;

  class ModuleLoader,M1_Server,Bare_Server,Weapon_Server,MovementManager,Commands,Permissions,CooldownManager,DamageManager,DataManager,KnockbackManager,MapManager,MovementManager,StunManager,Matter serverNode;
  class ModuleLoader2,Energy,M1_Client,Sol_Client,Movement,KnockbackHandler clientNode;
  class Space,Time universalNode;
```

### Functionality
(insert desc of every mechanic/module here later)

## Roadmap
- Add a state machine
- Merge `Bare_Server` and `Weapon_Server`
- Reduce collision latency
