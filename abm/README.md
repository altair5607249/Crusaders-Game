# Agent-Based Model (ABM)
Behold, Crusaders' simple ABM, which tests baseline character balance!

## Version History
| Version | Description | Status |
| --- | --- | --- |
| v1 | Bare-style-focused version. I designed the model + its agent behavior and directed the build, finding and fixing most of the problems myself. Much of the code was written with AI assistance (Claude and Gemini). | [Recovered](https://github.com/altair5607249/Crusaders-Game/blob/main/abm/abm_v1.ipynb?short_path=d9abe4e) |
| v2 | Weapon-style-focused version with batched matchups, per-move tallying, and a fixed RL wrapper. | Lost (not saved) |
| v3 | Full rewrite by me. I'm aware that the ABM code is rushed and messy, so I will be working on a full rewrite without AI! | In progress |

## Codebase
(insert flowchart here)  
(insert desc of components here)

## Constraints
- Time
  - Needed to be done in 2-3 days, so I could continue working on releasing Crusaders' open beta (v1 & v2)
- Scope
  - 1D simulations; only a single distance between agents
  - No auxiliary (aux) dash (v1 only)
- Estimations
  - Knockback and dash displacements are estimates from converting studs to fit 1D
  - Some moves' mechanics are simplified (e.g., Blue's/Bluee's Gamble)
  - Time moves in 0.1-second ticks, so moves with fast startups are rounded off and become inaccurate
- Agent Behavior
  - Agents pick moves using tag priority and randomness, not reinforcement learning (v1 only)
- Results' Meaning
  - Model output is not a proof of balance, and must be weighed against real playtest results
  - Against real playtest results, the model seems to be relatively accurate

## What is Agent-Based Modeling?
The University of Wisconsin-Madison (see [Agent-Based Evolutionary Game Dynamics](https://wisc.pb.unizin.org/agent-based-evolutionary-game-dynamics/chapter/i-3/)) has a lovely way of explaining this, so I'll be paraphrasing their content! 

Essentially, agent-based modeling is a way of simulating real-world systems. Such systems are made up by individual units (e.g., atoms, people, institutions) which repeatedly interact with each other and/or their environment!

## Why did I use Agent-Based Modeling?
Not because I enjoy torturing myself with my capriciousness, but for the love of the game (literally)!

I used basic intuition and experimental studies to balance the characters' stats, but I felt a little unconfident without empirical analysis to back up my numbers.

As I was researching ways to optimize the numbers with actual game theory, Agent-Based Modeling was one of the first and most promising solutions that came up!
