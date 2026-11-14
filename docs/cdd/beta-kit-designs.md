# Beta Kit Designs
These are the final kit designs for the open beta of Crusaders! 

Future versions will receive stat adjustments and (potentially) entire reworks, but the main idea established here will remain the same for each character.

## Notes
The general format of each character's section in this document is as follows:
- Character Overview
  - Configuration Tables — these numbers can be found in `Space`, `Time`, `M1_Server`, and the UI itself
    - Character Configs
    - M1 Configs
  - Moveset — for the specific data (e.g., damage, hitstun, knockback) attributed to each move, please refer to the [source code](https://github.com/altair5607249/Crusaders-Game/tree/main/src) itself
    - Bare Style
    - Weapon Style
   
Any mention of "SOL" in this document refers to the unique energy that lives within each individual and gives them life. If you wish to understand this intradiegetic concept better, you may refer to my [creative writing repo](https://github.com/altair5607249/Crusaders-Writing).

## Red
Also known as Aidalon, Red has an answer for everything! 

He's formidable in close-range combat, has powerful mid-range responses, can use shockwaves at a distance, and has explicit, defensive countermeasures against most attacks. Even his stats play to his general strength.

Though he's the roster's all-rounder, he possesses a special gimmick of his own: the lower his health gets, the stronger his moveset becomes. Whether this means adding a secondary effect to the move (e.g., bypassing parries), increasing the move's stats (e.g., damage), or leaving it the way it is (for character balance) is dependent on the nature of the move itself.

### Configuration Tables

#### Character Configs
| Stat | Amount |
| --- | --- |
| Max Health (HP) | 300 |
| Max Stamina (STA) | 150 |
| Walk Speed (studs/second) | 16 |
| Run Speed (studs/second) | 24 |

#### M1 Configs
| Stat | Bare Style | Weapon Style |
| --- | --- | --- |
| Damage (HP) | 5 | 6.25 |
| Range (studs) | 3.5 | 5.5 |
| Delay (seconds) | 0.2 | 0.2 |
| Finisher Delay (seconds) | 0.2 | 0.2 |
| Cooldown (seconds) | 0.399 | 0.399 |
| Finisher Cooldown (seconds) | 2.249 | 2.249 |
| Hitstun (seconds) | 0.6 | 0.6 |
| Finisher Hitstun (seconds) | 0.0 | 0.0 |
| Extension (seconds) | 0.9 | 0.9 |

### Moveset

#### Bare Style
| Move # | Move Name | Description |
| --- | --- | --- |
| [Move 1](https://github.com/altair5607249/Crusaders-Game/blob/main/src/ServerScriptService/ModuleLoader/OutputModules/Bare_Server/CharModules/Redd/Move1/init.luau) | Headbutt | Red swiftly smashes his head forward. When his health is below 50% of its maximum value, this move is able to bypass parrying. |
| [Move 2](https://github.com/altair5607249/Crusaders-Game/blob/main/src/ServerScriptService/ModuleLoader/OutputModules/Bare_Server/CharModules/Redd/Move2/init.luau) | Hero's Fist | Red reinforces his right fist with his SOL before throwing it forward, creating a massive shockwave in the process. This move's damage scales higher with lower health. When his health is below 20% of its maximum value, this move is able to bypass parrying. |
| [Move 3](https://github.com/altair5607249/Crusaders-Game/blob/main/src/ServerScriptService/ModuleLoader/OutputModules/Bare_Server/CharModules/Redd/Move3/init.luau) | Sacred Circle | Red summons a ring of fire around himself that radiates symmetrically. |
| [Move 4](https://github.com/altair5607249/Crusaders-Game/blob/main/src/ServerScriptService/ModuleLoader/OutputModules/Bare_Server/CharModules/Redd/Move4/init.luau) | Sixth Sense | Red becomes massless, gaining immunity to all attacks; he also has the opportunity to equip his weapon, effectively switching from bare style to weapon style. This move's immunity duration scales higher with lower health. |

#### Weapon Style
| Move # | Move Name | Description |
| --- | --- | --- |
| [Move 1](https://github.com/altair5607249/Crusaders-Game/blob/main/src/ServerScriptService/ModuleLoader/OutputModules/Weapon_Server/CharModules/Redd/Move1/init.luau) | Feint | Red pretends to use Supernova, but swipes his hand forward at the last moment. |
| [Move 2](https://github.com/altair5607249/Crusaders-Game/blob/main/src/ServerScriptService/ModuleLoader/OutputModules/Weapon_Server/CharModules/Redd/Move2/init.luau) | Supernova | Red builds up SOL in his knife before spinning in a circle with it, releasing all of its destructive energy in a brilliant explosion; he nearly passes out afterward. This move's damage scales higher with lower health. |
| [Move 3](https://github.com/altair5607249/Crusaders-Game/blob/main/src/ServerScriptService/ModuleLoader/OutputModules/Weapon_Server/CharModules/Redd/Move3/init.luau) | Blade Parade | Red telekinetically throws his knife around himself, its trajectory radiating symmetrically. |
| [Move 4](https://github.com/altair5607249/Crusaders-Game/blob/main/src/ServerScriptService/ModuleLoader/OutputModules/Weapon_Server/CharModules/Redd/Move4/init.luau) | Chanticleer Counter | Red substitutes himself with his pet rooster, which proportionally reflects all damage administered to it. The proportion of reflected damage scales higher with lower health. |

## Orange

Sorry, but I haven't figured this character out yet; check back later!

## Yellow
Also known as Ethandros, Yellow can outpace any plan!

There's no time to waste against him, as he can chip away at your health from the comfort of his corner; even backing him up into an actual corner may simply prompt him to run away.

His whole thing is being fast, whether through the timing of his moves, his actual movement, or his general playstyle. Of course, the main downside to his kit is that he's quite frail, so it's best to keep some distance when playing as him; he performs best at farther ranges, having minimal coverage for close to mid-range combat.

### Configuration Tables

#### Character Configs
| Stat | Amount |
| --- | --- |
| Max Health (HP) | 250 |
| Max Stamina (STA) | 175 |
| Walk Speed (studs/second) | 15.5 |
| Run Speed (studs/second) | 25 |

#### M1 Configs
| Stat | Bare Style | Weapon Style |
| --- | --- | --- |
| Damage (HP) | 4.85 | 5.7 |
| Range (studs) | 3.5 | 7 |
| Delay (seconds) | 0.15 | 0.15 |
| Finisher Delay (seconds) | 0.3 | 0.3 |
| Cooldown (seconds) | 0.299 | 0.299 |
| Finisher Cooldown (seconds) | 1.999 | 1.999 |
| Hitstun (seconds) | 0.3 | 0.3 |
| Finisher Hitstun (seconds) | 0.5 | 0.5 |
| Extension (seconds) | 0.8 | 0.8 |

### Moveset

#### Bare Style
| Move # | Move Name | Description |
| --- | --- | --- |
| [Move 1](https://github.com/altair5607249/Crusaders-Game/blob/main/src/ServerScriptService/ModuleLoader/OutputModules/Bare_Server/CharModules/Yello/Move1/init.luau) | Beam | Yellow shoots a beam of his SOL's destructive energy forward. |
| [Move 2](https://github.com/altair5607249/Crusaders-Game/blob/main/src/ServerScriptService/ModuleLoader/OutputModules/Bare_Server/CharModules/Yello/Move2/init.luau) | Invisible Attack | Yellow kicks forward faster than the eye can perceive. |
| [Move 3](https://github.com/altair5607249/Crusaders-Game/blob/main/src/ServerScriptService/ModuleLoader/OutputModules/Bare_Server/CharModules/Yello/Move3/init.luau) | Fulmination | Yellow leaps up and smashes the ground with the force of a thunderbolt, damaging the surrounding area. |
| [Move 4](https://github.com/altair5607249/Crusaders-Game/blob/main/src/ServerScriptService/ModuleLoader/OutputModules/Bare_Server/CharModules/Yello/Move4/init.luau) | Rift Rush | Yellow quickly summons a pair of portals, instantly traveling forward through them. |

#### Weapon Style
| Move # | Move Name | Description |
| --- | --- | --- |
| Move 1 | Lasso | Yellow slings his yoyo forward, roping in anyone caught by it. |
| Move 2 | Lighthouse | Yellow opens his SOL, surrounding himself with a blinding light that stuns anyone close enough. |
| Move 3 | Breakaway | Yellow performs a yoyo trick, tossing it forward in a wide motion. (Note: I know the yoyo is supposed to be tossed to the side of the yo-yoer, but I somehow forgot to animate it that way! I will rectify this in a future update, of course.) |
| Move 4 | Borean Blitz | Yellow strengthens his body with his SOL, moving with incredible speed; his weapon-style moveset is enhanced during this strengthened state, and all successful hits (including M1s) restore stamina. |

## Green
Also known as Zakyros, Green won't go down without a fight!

He's got a few tricks up his sleeve to make sure his opponents won't escape unscathed; not only is he tanky, but he can steal health and utilize a shield. That all goes without even mentioning his grab!

Being the type of fighter he is, there is a key benefit to keeping him at high health: his moveset becomes stronger. He practically follows the same principle that Red does with low health, though that does lead to the implication that he grows weaker as he loses more health, which is true.

### Configuration Tables

#### Character Configs
| Stat | Amount |
| --- | --- |
| Max Health (HP) | 325 |
| Max Stamina (STA) | 100 |
| Walk Speed (studs/second) | 17 |
| Run Speed (studs/second) | 22 |

#### M1 Configs
| Stat | Bare Style | Weapon Style |
| --- | --- | --- |
| Damage (HP) | 4.95 | 5.9 |
| Range (studs) | 3.5 | 6.25 |
| Delay (seconds) | 0.25 | 0.25 |
| Finisher Delay (seconds) | 0.25 | 0.25 |
| Cooldown (seconds) | 0.499 | 0.499 |
| Finisher Cooldown (seconds) | 2.499 | 2.499 |
| Hitstun (seconds) | 0.55 | 0.55 |
| Finisher Hitstun (seconds) | 0.0 | 0.0 |
| Extension (seconds) | 1 | 1 |

### Moveset

#### Bare Style
| Move # | Move Name | Description |
| --- | --- | --- |
| [Move 1](https://github.com/altair5607249/Crusaders-Game/blob/main/src/ServerScriptService/ModuleLoader/OutputModules/Bare_Server/CharModules/Gleen/Move1/init.luau) | Suplex | Green grabs the opponent in front of him if there is one, and slams them onto the ground behind himself. |
| [Move 2](https://github.com/altair5607249/Crusaders-Game/blob/main/src/ServerScriptService/ModuleLoader/OutputModules/Bare_Server/CharModules/Gleen/Move2/init.luau) | Animal Instinct | Green laughs and locks onto the nearest opponent if one is in range, swinging violently at them. This move's damage scales higher with higher health. |
| [Move 3](https://github.com/altair5607249/Crusaders-Game/blob/main/src/ServerScriptService/ModuleLoader/OutputModules/Bare_Server/CharModules/Gleen/Move3/init.luau) | Give Gifts | Green prays to the past and repositions himself behind the nearest opponent if one is in range, stealing their health. This move's heal scales higher with lower health. |
| [Move 4](https://github.com/altair5607249/Crusaders-Game/blob/main/src/ServerScriptService/ModuleLoader/OutputModules/Bare_Server/CharModules/Gleen/Move4/init.luau) | Breach | Green propels himself forward with his SOL for a period of time, during which his trajectory changes with wherever he's facing; he stops early if he hits an opponent. |

#### Weapon Style
| Move # | Move Name | Description |
| --- | --- | --- |
| [Move 1](https://github.com/altair5607249/Crusaders-Game/blob/main/src/ServerScriptService/ModuleLoader/OutputModules/Weapon_Server/CharModules/Gleen/Move1/init.luau) | Yeet | Green hurls his anchor forward; anything penetrated by the tip is dealt with triple the damage. |
| [Move 2](https://github.com/altair5607249/Crusaders-Game/blob/main/src/ServerScriptService/ModuleLoader/OutputModules/Weapon_Server/CharModules/Gleen/Move2/init.luau) | Accretion Disk | Green swings his anchor around himself in a circle. This move drains the stamina of whomever it hits. |
| [Move 3](https://github.com/altair5607249/Crusaders-Game/blob/main/src/ServerScriptService/ModuleLoader/OutputModules/Weapon_Server/CharModules/Gleen/Move3/init.luau) | Anchor Point | Green shields himself in the direction he's facing with his anchor; he's able to move while his shield is up. The strength of the shield scales higher with higher health. |
| [Move 4](https://github.com/altair5607249/Crusaders-Game/blob/main/src/ServerScriptService/ModuleLoader/OutputModules/Weapon_Server/CharModules/Gleen/Move4/init.luau) | Ghillie Groundbreaker | Green leaps forward and smashes the ground beneath him as he lands. When his stamina is equal to this move's cost, the damage diminishes by 20%; when his stamina is lesser than the cost, the damage diminishes by 40% and the effective radius is halved. |

## Blue
Also known as Gabrius, Blue is nearly impossible to predict!

If you think the other characters have tricks, this guy is the entire magic show. He can copy his opponents, gamble with them, and even mess with their cooldowns. I've had to add numerous features to the codebase (e.g., cooldown manipulation) just because of him!

He can play effectively at any range, though his heaviest-hitting moves prefer narrow spaces. Without experience, you're bound to be confused by him at least once. Once you've fought him enough times, his tricks can be countered by your mindfulness, though knowing his playstyle doesn't make him any less dangerous.

### Configuration Tables

#### Character Configs
| Stat | Amount |
| --- | --- |
| Max Health (HP) | 275 |
| Max Stamina (STA) | 125 |
| Walk Speed (studs/second) | 16.5 |
| Run Speed (studs/second) | 23 |

#### M1 Configs
| Stat | Bare Style | Weapon Style |
| --- | --- | --- |
| Damage (HP) | 4.9 | 5.9 |
| Range (studs) | 3.5 | 6 |
| Delay (seconds) | 0.2 | 0.2 |
| Finisher Delay (seconds) | 0.2 | 0.2 |
| Cooldown (seconds) | 0.399 | 0.399 |
| Finisher Cooldown (seconds) | 2.249 | 2.249 |
| Hitstun (seconds) | 0.55 | 0.55 |
| Finisher Hitstun (seconds) | 0.0 | 0.0 |
| Extension (seconds) | 0.9 | 0.9 |

### Moveset

#### Bare Style
| Move # | Move Name | Description |
| --- | --- | --- |
| [Move 1](https://github.com/altair5607249/Crusaders-Game/blob/main/src/ServerScriptService/ModuleLoader/OutputModules/Bare_Server/CharModules/Bluee/Move1/init.luau) | Rip | Blue cleaves the air with his hand, creating a temporary, spatial rip in front of himself. |
| [Move 2](https://github.com/altair5607249/Crusaders-Game/tree/main/src/ServerScriptService/ModuleLoader/OutputModules/Bare_Server/CharModules/Bluee/Move2/init.luau) | Copy | Blue warps his SOL, allowing himself to perform the other characters' moves. He can only copy one, random move at a time; the pool of available moves does not include any weapon-style moves, nor the fourth bare-style move of other characters. |
| [Move 3](https://github.com/altair5607249/Crusaders-Game/tree/main/src/ServerScriptService/ModuleLoader/OutputModules/Bare_Server/CharModules/Bluee/Move3/init.luau) | Vortex | Blue spins and sucks in every opponent if there are any in range. |
| [Move 4](https://github.com/altair5607249/Crusaders-Game/tree/main/src/ServerScriptService/ModuleLoader/OutputModules/Bare_Server/CharModules/Bluee/Move4/init.luau) | Gamble | Blue offers to gamble with the nearest opponent if one is in range; the gamble at hand is a coin flip. Whoever fails the coin flip loses an eighth of their current health and is left stunned. If both players pick the same option, nothing happens. If both players lose after picking different options, they're both left stunned. |

#### Weapon Style
| Move # | Move Name | Description |
| --- | --- | --- |
| [Move 1](https://github.com/altair5607249/Crusaders-Game/blob/main/src/ServerScriptService/ModuleLoader/OutputModules/Weapon_Server/CharModules/Bluee/Move1/init.luau) | Rend | Blue dashes forward and swings his sword, creating a narrow shockwave in the process. |
| [Move 2](https://github.com/altair5607249/Crusaders-Game/blob/main/src/ServerScriptService/ModuleLoader/OutputModules/Weapon_Server/CharModules/Bluee/Move2/init.luau) | Oumuamua | Blue ends one of his moves' cooldowns early; the pool of available moves does not include any bare-style moves. If none of his moves are on cooldown, he performs a variant of this move called "Azurewrath," in which he adds cooldown to a random move of the nearest opponent if one is in range; the pool of available moves depends on the opponent's current fighting style. |
| [Move 3](https://github.com/altair5607249/Crusaders-Game/blob/main/src/ServerScriptService/ModuleLoader/OutputModules/Weapon_Server/CharModules/Bluee/Move3/init.luau) | Sword Trick | Blue performs a series of forward slashes with his sword. |
| [Move 4](https://github.com/altair5607249/Crusaders-Game/blob/main/src/ServerScriptService/ModuleLoader/OutputModules/Weapon_Server/CharModules/Bluee/Move4/init.luau) | Protean Pace | Blue channels his SOL through his sword and releases its destructive energy forward, which takes different forms depending on his health: If his health is above or equal to 66% of its maximum value, it becomes ice; if his health is between 66% and 33% of its maximum value (or equal to 33%), it becomes water; if his health is below 33% of its maximum value, it becomes vapor. |

## Purple

Sorry, but I haven't figured this character out yet; check back later!
