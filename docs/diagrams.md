# Codebase
Important parts will be given in smaller diagrams, and everything, everywhere, all at once will be visible in the final diagram.

## Legend
- Connections
  - Solid Line — Relation
  - Solid Arrow — Require
    - Arrow labels may specify otherwise, such as the following:
      - RE — Remote Event
      - IA — Input Action
  - Thick Arrow — Init
- Colors
  - Red — Event
  - Blue — Client
  - Green — Server
  - Purple — Universal
- Shapes (standards derived from [ISO 5807:1985](https://cdn.standards.iteh.ai/samples/11955/1b7dd254a2a54fd7a89d616dc0570e18/ISO-5807-1985.pdf))
  - Rounded Rectangle — terminator; the start or end of the program
  - Rectangle — process; an action or task
  - Rhombus — decision; yes/no branch point
  - Ray — flow line; direction of the program's sequence
 
## Initialization
```mermaid
flowchart TB;

  classDef eventNode fill:#e33939,stroke:#000000,color:#000000
  classDef serverNode fill:#5bf547,stroke:#000000,color:#000000
  classDef clientNode fill:#42a1f5,stroke:#000000,color:#000000
  classDef universalNode fill:#b549eb,stroke:#000000,color:#000000

  subgraph StarterPlayerScripts
    ModuleLoader2;
    Energy;

    subgraph Handlers
      AnimationHandler;
      KnockbackHandler;
      MusicHandler;
    end

    subgraph InputModules
      M1_Client;
      Sol_Client;
      Movement;
    end
  end

  subgraph StarterGui
    subgraph Transition
      ModuleLoader3==>A["Manager"]
    end
  end

  subgraph ServerScriptService
    ModuleLoader;
    Matter;

    subgraph a["Everything Else"]
      b["Lots of Modules"];
    end
  end

  c["Player joins"]==>ModuleLoader2

  A==>|Loading screen is removed| ModuleLoader2

  ModuleLoader2-->|RE| Matter-->d["Player appears"];
  ModuleLoader2==>Energy==>InputModules;
  ModuleLoader2==>KnockbackHandler;
  ModuleLoader2==>MusicHandler;

  ModuleLoader==>Matter;
  ModuleLoader==>a;

  class c,d eventNode;
  class ModuleLoader,Matter,b,CooldownManager,DamageManager,DataManager,KnockbackManager,MapManager,MovementManager,StunManager,M1_Server,Bare_Server,Weapon_Server serverNode;
  class ModuleLoader2,Energy,AnimationHandler,KnockbackHandler,MusicHandler,M1_Client,Sol_Client,Movement,ModuleLoader3,ModuleLoader4,A,B,C clientNode;
  class Space,Time universalNode;
```

## Input Action System (IAS)
```mermaid
flowchart TB;

  classDef eventNode fill:#e33939,stroke:#000000,color:#000000
  classDef clientNode fill:#42a1f5,stroke:#000000,color:#000000

  subgraph StarterPlayerScripts
    Energy;

    subgraph InputModules
      M1_Client;
      Sol_Client;
      Movement;
    end
  end

  Energy-->InputModules
  InputModules-->|Send input-action data| Energy
  Energy-->|First iteration| A{Is the action valid?}

  A-->|No| B["Warning"]-->|Next iteration| A
  A-->|Yes| C["Press connection is created"]

  C-->D["Connection is saved"]
  D-->E{Is this a held action?}

  E-->|Yes| F["Release connection is created"]-->f["Connection is saved"]-->H["Action is mapped to GUI buttons"]
  E-->|No| G-->H

  G-->|Only for the first valid iteration| h["Set listener"]
  f-->|Only for the first valid iteration| h
  h-->i["Player dies & respawns"]-->H

  G-->a["Associated context is tagged as active"]
  f-->a
  a-->|Next iteration| A

  H-->I{Are the button and the binding valid?}

  I-->|No| J("End iteration")
  I-->|Yes| K{Is this a held action?}

  K-->|No| L["Activated connection is created"]-->O["Connection(s) saved"]
  K--> |Yes| M["Began & ended connections are created"]-->O

  O-->|Next iteration| H

  class Energy,M1_Client,Sol_Client,Movement clientNode;
  class i eventNode;
```

## Client-Server Communication
```mermaid
flowchart TB;

  classDef serverNode fill:#5bf547,stroke:#000000,color:#000000
  classDef clientNode fill:#42a1f5,stroke:#000000,color:#000000

  subgraph StarterPlayerScripts
    Energy;

    subgraph InputModules
      M1_Client;
      Sol_Client;
      Movement;
    end
  end

  subgraph ServerScriptService
    ModuleLoader;

    subgraph Managers
      MovementManager;
    end

    subgraph OutputModules
      M1_Server;
      Bare_Server;
      Weapon_Server;
    end
  end

  Energy==>InputModules

  M1_Client-->|RE| ModuleLoader
  Sol_Client-->|RE| ModuleLoader
  Movement-->|RE| MovementManager

  ModuleLoader-->OutputModules

  class ModuleLoader,MovementManager,M1_Server,Bare_Server,Weapon_Server serverNode;
  class Energy,M1_Client,Sol_Client,Movement clientNode;
```

## Combat Flow
```mermaid
flowchart TB;

  classDef eventNode fill:#e33939,stroke:#000000,color:#000000
  classDef serverNode fill:#5bf547,stroke:#000000,color:#000000
  classDef clientNode fill:#42a1f5,stroke:#000000,color:#000000
  classDef universalNode fill:#b549eb,stroke:#000000,color:#000000

  subgraph StarterPlayerScripts
    subgraph InputModules
      M1_Client;
      Sol_Client;
      Movement;
    end
  
    Player-Input-->|IA| M1_Client;
    Player-Input-->|IA| Sol_Client;
    Player-Input-->|IA| Movement;
  end

  M1_Client-->|RE| ModuleLoader;
  Sol_Client-->|RE| ModuleLoader;
  Movement

  subgraph ServerScriptService
    ModuleLoader;

    subgraph Managers
      CooldownManager;
    end

    subgraph OutputModules
      M1_Server;
      Bare_Server;
      Weapon_Server;
    end
  
    subgraph Managers
      DamageManager;
      MovementManager;
    end
  
    ModuleLoader-->|M1| M1_Server
    ModuleLoader-->|Sol| Bare_Server
    ModuleLoader-->|Sol| Weapon_Server
  end

  subgraph ReplicatedStorage
    subgraph UniversalModules
      Space;
      Time;
    end
  end

  OutputModules-->Space;
  OutputModules-->Time;

  M1_Server-->CooldownManager;
  Bare_Server-->CooldownManager;
  Weapon_Server-->CooldownManager;

  M1_Server-->DamageManager;
  Bare_Server-->DamageManager;
  Weapon_Server-->DamageManager;

  InputModules-->Time;
  Movement-->Space;
  Movement-->|RE; Anticheat| MovementManager;

  class Player-Input eventNode;
  class ModuleLoader,M1_Server,Bare_Server,Weapon_Server,DamageManager,CooldownManager,MovementManager serverNode;
  class ModuleLoader2,M1_Client,Sol_Client,Movement,KnockbackHandler clientNode;
  class Space,Time universalNode;
```

## Bare-Style Flow
```mermaid
flowchart TB;

  classDef serverNode fill:#5bf547,stroke:#000000,color:#000000
  classDef clientNode fill:#42a1f5,stroke:#000000,color:#000000
  classDef universalNode fill:#b549eb,stroke:#000000,color:#000000

  classDef redNode fill:#ff9191,stroke:#000000,color:#000000
  classDef yellowNode fill:#fdff91,stroke:#000000,color:#000000
  classDef greenNode fill:#91ff9c,stroke:#000000,color:#000000
  classDef blueNode fill:#91b8ff,stroke:#000000,color:#000000

  subgraph ServerScriptService
    subgraph Managers
      DamageManager;
    end

    subgraph OutputModules
      Bare_Server;
    end

    Bare_Server---CharModules

    subgraph CharModules
      subgraph Redd
        A["Move1"]-->DamageManager;
        B["Move2"]-->DamageManager;
        C["Move3"]-->DamageManager;
        D["Move4"];
      end 
      subgraph Yello
        E["Move1"]-->DamageManager;
        F["Move2"]-->DamageManager;
        G["Move3"]-->DamageManager;
        H["Move4"]-->DamageManager;
      end
      subgraph Gleen
        I["Move1"]-->DamageManager;
        J["Move2"]-->DamageManager;
        K["Move3"]-->DamageManager;
        L["Move4"]-->DamageManager;
      end 
      subgraph Bluee
        M["Move1"]-->DamageManager;
        N["Move2"];
        O["Move3"]-->DamageManager;
        P["Move4"];
      end 
    end
  end

  subgraph ReplicatedStorage
    subgraph UniversalModules
      Space;
      Time;
    end
  end

  Bare_Server-->UniversalModules;
  OutputModules-->Time;

  D-->Space;
  J-->Space;
  L-->Space;
  O-->Space;

  class ModuleLoader,M1_Server,Bare_Server,Weapon_Server,MovementManager,DamageManager,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,KnockbackManager,StunManager serverNode;
  class ModuleLoader2,Player-Input,M1_Client,Sol_Client,Movement,KnockbackHandler clientNode;
  class Space,Time universalNode;

  class Redd redNode;
  class Yello yellowNode;
  class Gleen greenNode;
  class Bluee blueNode;
```

## Weapon-Style Flow
```mermaid
flowchart TB;

  classDef serverNode fill:#5bf547,stroke:#000000,color:#000000
  classDef clientNode fill:#42a1f5,stroke:#000000,color:#000000
  classDef universalNode fill:#b549eb,stroke:#000000,color:#000000

  classDef redNode fill:#ff9191,stroke:#000000,color:#000000
  classDef yellowNode fill:#fdff91,stroke:#000000,color:#000000
  classDef greenNode fill:#91ff9c,stroke:#000000,color:#000000
  classDef blueNode fill:#91b8ff,stroke:#000000,color:#000000

  subgraph ServerScriptService
    subgraph Managers
      DamageManager;
    end

    subgraph OutputModules
      Weapon_Server;
    end

    Weapon_Server---CharModules

    subgraph CharModules
      subgraph Redd
        Q["Move1"]-->DamageManager;
        R["Move2"]-->DamageManager;
        S["Move3"]-->DamageManager;
        T["Move4"];
      end 
      subgraph Yello
        U["Move1"]-->DamageManager;
        V["Move2"]-->DamageManager;
        W["Move3"]-->DamageManager;
        X["Move4"];
      end 
      subgraph Gleen
        Y["Move1"]-->DamageManager;
        Z["Move2"]-->DamageManager;
        a["Move3"];
        b["Move4"]-->DamageManager;
        end 
      subgraph Bluee
        c["Move1"]-->DamageManager;
        d["Move2"]-->DamageManager;
        e["Move3"]-->DamageManager;
        f["Move4"]-->DamageManager;
      end 
    end
  end

  subgraph ReplicatedStorage
    subgraph UniversalModules
      Space;
      Time;
    end
  end

  Weapon_Server-->UniversalModules;
  OutputModules-->Time;

  X-->Space;
  a-->Space;
  b-->Space;
  
  class ModuleLoader,M1_Server,Bare_Server,Weapon_Server,MovementManager,DamageManager,Q,R,S,T,U,V,W,X,Y,Z,a,b,c,d,e,f,KnockbackManager,StunManager serverNode;
  class ModuleLoader2,Player-Input,M1_Client,Sol_Client,Movement,KnockbackHandler clientNode;
  class Space,Time universalNode;

  class Redd redNode;
  class Yello yellowNode;
  class Gleen greenNode;
  class Bluee blueNode;
```

## Full System Diagram
```mermaid
flowchart TB;

  classDef serverNode fill:#5bf547,stroke:#000000,color:#000000
  classDef clientNode fill:#42a1f5,stroke:#000000,color:#000000
  classDef universalNode fill:#b549eb,stroke:#000000,color:#000000

  subgraph StarterPlayerScripts
    ModuleLoader2==>Energy;
    ModuleLoader2==>Handlers;
    Energy==>InputModules;
  
    subgraph Handlers
      AnimationHandler;
      KnockbackHandler;
      MusicHandler;
    end
  
    subgraph InputModules
      M1_Client;
      Sol_Client;
      Movement;
    end
  end

  ModuleLoader2-->|RE| Matter;

  M1_Client-->AnimationHandler;
  Sol_Client-->AnimationHandler;
  M1_Client-->|RE| ModuleLoader;
  Sol_Client-->|RE| ModuleLoader;
  Movement-->|RE| MovementManager;
  InputModules-->Time;
  Movement-->Space;

  subgraph ReplicatedStorage
    subgraph UniversalModules
      Space;
      Time;
    end
  end

  ModuleLoader==>Administration;
  ModuleLoader==>Managers;
  ModuleLoader==>OutputModules;
  ModuleLoader==>Matter;
  MapManager-->Matter;

  subgraph ServerScriptService
    ModuleLoader;
    Matter;

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
  end

  CooldownManager-->Time;
  DamageManager-->Space;
  DamageManager-->DataManager;
  DamageManager-->KnockbackManager;
  DamageManager-->StunManager;
  M1_Server-->Time;
  Bare_Server-->Time;
  Weapon_Server-->Time;
  StunManager-->Space;
  StunManager-->Time;
  M1_Server-->Space;
  Bare_Server-->Space;
  Weapon_Server-->Space;
  KnockbackManager-->Space;
  KnockbackManager-->|RE| ModuleLoader2;
  ModuleLoader2-->KnockbackHandler;
  ModuleLoader2-->MusicHandler;
  MovementManager-->Space;
  MovementManager-->Time;
  MovementManager-->CooldownManager;
  MovementManager-->StunManager;

  subgraph StarterGui
    subgraph Transition
      ModuleLoader3==>A["Manager"]
    end

    subgraph Selection
      B["Manager"]
    end

    subgraph Settings
      ModuleLoader4==>C["Manager"]
    end
  end

  Matter-->|RE| ModuleLoader3-->A;
  DataManager-->|RE| C-->|RE| DataManager;
  B-->|RE| ModuleLoader-->Matter;

  OutputModules-->CooldownManager;
  Bare_Server-->StunManager;
  Weapon_Server-->StunManager;

  class ModuleLoader,M1_Server,Bare_Server,Weapon_Server,MovementManager,Commands,Permissions,CooldownManager,DamageManager,DataManager,KnockbackManager,MapManager,MovementManager,StunManager,Matter serverNode;
  class ModuleLoader2,Energy,M1_Client,Sol_Client,Movement,AnimationHandler,KnockbackHandler,MusicHandler,ModuleLoader3,ModuleLoader4,A,B,C clientNode;
  class Space,Time universalNode;
```
