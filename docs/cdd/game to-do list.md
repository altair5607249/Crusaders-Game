Notes:

- Weapon M1s & moves will drain this faster than the Bare M1s & moves  
- Weapon M1s & moves will fill this faster than the Bare M1s & moves  
- Each character will have a preferred motif/element behind their moveset, despite their omniproficiency in the lore (e.g., Red \= Fire)  
- With RBM3 (both normal and ult variant), remember to temporarily spawn the fire circle decal from Sword Fight on the Heights for the visual wrapper  
- Obviously the visuals of the ults will be cooler, and the damage magnitude and range will scale higher; massive stamina drawback though  
- Only 2 (im considering making this 1 tho…) ult moves should be allowed per duration  
- There is a common theme with the move ordering:  
  - 1 \= Actual, In-Lore Moves  
  - 2 \= Lookism Tribute  
  - 3 \= Of Their Elemental Motif  
  - 4 \= Gimmicky/Archetypal  
- Each server has 4 spots, and will only allow one player per character  
  - This will increase to 6 once I push out phase two of this game (after college apps)

- P.S. Yes this game CAN encourage jumping/teaming IF done correctly (though ill put measures to regulate this in future updates) as seen by certain moves, such as GBM3   
  - There’s method in my madness trust\!\!

To Program:

- [x] ~~Fix the UnmanagedManagers architecture~~  
- [x] ~~Create a DataManager (module) that handles the repetitive onCharacterChanged thing \+ server-side registries~~  
- [ ] Fix the ModuleLoader2 architecture  
- [ ] Integrate anticheats (for movement \+ knockback)  
- [x] ~~Refine knockback physics~~  
- [ ] Implement ragdoll physics  
  - [ ] smth about changing the motor6d joints to ballsocketconstraints  
- [x] ~~Rework shockwave integration into DamageManager~~  
- [x] ~~Refine stun logic~~  
- [ ] Stamina Meter  
- [ ] Ult Meter  
- [x] ~~Make a server-side movement module (which enables i-frames)~~  
- [ ] Include a way for damaging opponents to interrupt their attack if loading

Gimmicks:

* Redd: Less health \= more damage (berserker)  
* Yello: Quick recovery \+ cooldowns (striker)  
* Gleen: More health \= more damage (paladin)  
* Bluee: Unpredictable (trickster)

- [ ] Aidan’s Moveset  
  - [ ] Bare  
    - [x] ~~Headbutt (self-explanatory; damage scales higher with how low his health is)~~  
      * Ult Variant: Groin Strike (will have a custom stun \[\~5?\] that’s higher than everything else in the game lol; start-up animation will vary, and WILL imitate other start-up animations)  
    - [x] ~~Hero’s Fist (it also has a shockwave \[strength scales higher with how low his health is\], so technically two damage module calls; both can be received if you’re close enough)~~  
      * Ult Variant: Supernova (the attacker is blinded for half of its duration if within the shockwave’s range)  
    - [x] ~~Sacred Circle (summons a ring of fire around his player model for 2.5 \[scales higher with how low his health is\] seconds; his fire damages himself when he’s not in ult form)~~  
      * Ult Variant: Insane Flame (the fire now chases the player for half of its duration)  
    - [x] ~~Sixth Sense (dodge anything \[except ult moves\] for 1.5 \[scales higher with how low his health is\] seconds)~~  
      * Ult Variant: Wordless Willpower (counter anything \+ insta kill)  
  - [ ] Weapon: Bombastic Blades (pulls an arsenal of blades from his body which he can switch between) \+ Rubber Rooster of Reckoning (for his gimmick move)  
    - [ ] Feint  
    - [ ] Event Horizon; emulates a black hole for 1 second  
    - [ ] Blade Parade  
    - [ ] Chanticleer Counter; reflects dmg

- [ ] My Moveset  
  - [ ] Bare  
    - [x] ~~Beam (spammable ranged attack that lightly stuns \+ knocks back)~~  
      * Ult Variant: Railgun (shoots eight dimension-breaking blasts that ignores distance)  
    - [x] ~~Invisible Attack (shortest start-up in the game \[\~0.1 seconds?\])~~  
      * Ult Variant: Don’t Blink\! (no start-up/depends on ping \+ sure-hit that locks onto and blitzes through the opponent \[unless the an opponent’s active move is too gimmicky {only example i can currently think of is Wordless Willpower}\], but will have a decent cooldown and consumes a third of Yello’s stamina)  
    - [x] ~~Fulmination (damage every opponent within radius \+ custom stun \[yes this applies to the ult\])~~  
      * Ult Variant: Luminous Jet (no start-up/depends on ping \+ damages every opponent within radius \[now larger\])  
    - [x] ~~Rift Rush (Yello “teleports” forward \~20 studs)~~  
      * Ult Variant: Dimension Drift (transports Yello to a space between dimensions for \~5? seconds, allowing him to move around freely and peer into the physical realm while being invisible to it)  
  - [ ] Weapon: Yearnful Yoyo of Yesterday  
    - [ ] Lasso; long-range, pulls the opponent in  
    - [ ] Strobe; disorients the opponent (only close-range use)  
    - [ ] Breakaway; mid-range boomerang type of move  
    - [ ] Godspeed; utility

- [ ] Zachary’s Moveset  
  - [ ] Bare  
    - [ ] Suplex (requires really close range \[damage scales higher with how high his health is\])  
      * Ult Variant: Bare Bones (more ssireum based and grabs the literal bone\[s\] of the opponent to grab and slam them, dealing more damage and having a custom stun \[MUCH lower than the groin strike though)  
    - [ ] Animal Instinct (takes 30% less damage \[scales higher with how high his health is\] for 3 seconds, but forces him to rush at the opponent’s model for that duration)  
      * Ult Variant: Monster (same thing but 30% now starts at 45% \+ he rushes at the opponent for 2 seconds instead of 3 and is not liable to heavy stun \[only custom stun\])  
    - [ ] Give Gifts (lifesteals and redistributes health \[yes you can just choose to heal yourself in future updates\], and the amount stolen scales higher with how high his health is)  
      * Ult Variant: Give Life (place a marker on your player of choice \[can be yourself\] for a certain time period \[scales higher with higher health\], and if the player dies in that time period, they resurrect and resist full death)  
    - [ ] Breach (battering ram into your opponent \[lasts \~1.5 seconds until running out if a “hit” hasn’t been performed\], which also cancels out their move \[assuming it isn’t an ult or too gimmicky, aka the BM4s and WM4s\])  
      * Ult Variant: Vital Vanguard (cancels out almost any opponent’s move upon hitting the opponent, lasts longer \[\~4 secs?\] until a hit is performed, and now slows the opponent down \[effect is halved if they’re in ult\])  
  - [ ] Weapon: Gallant Grip of Gravity  
    - [ ] Yeet (green launches the anchor forward allowing for a ranged attack, people within the outer hitbox of the anchor while thrown are stunned. While people directly hit by the anchor are launched backward with it causing 15% max health damage. VERY small window for direct hit.)  
    - [ ] Accretion Disk (A spinning attack which green swings his anchor around him by the rope loop, allowing for knockback with minimal damage, every time an enemy is hit stamina is decreased by 5 and spin speed decreases)  
    - [ ] Anchor Point (can use anchor as a shield with limited durability, cant use abilities, mainly for regaining stamina while low or depleted, if shield breaks it applies a brief stun to green. Only blocks attacks from the front, and decreases aoe attack damage)  
    - [ ] Breach 2 (w/ anchor dlc)

- [ ] Gabriel’s Moveset  
  - [ ] Bare  
    - [ ] Rend (creates a shockwave that matches his lookvector and ignores distance, which means damage does not depend on the range unlike Hero’s Fist \[+ more narrow in trajectory compared to Hero’s Fist\])  
      * Ult Variant: Sunder (cuts relative to the lookvector \[slightly wider trajectory\], reaching across the entire, given map)  
    - [ ] Copy (copies a random move from the queried character, except ult moves and certain normal moves \[probably the BM4s & WM4s\])  
      * Ult Variant: Sublimate (copies anything and improves upon its \[number-based, because im not a god at coding\] mechanics, except for certain, genuinely incompatible/gimmicky moves)  
    - [ ] Vortex (Bluee is granted resistance and rushes forth \[by lookvector\] for 2.5 seconds, dealing damage from a hitbox relative to his character model \[think of a water vortex\])  
      * Ult Variant: Typhoon (same thing, but lasts for 4 seconds and may now send the opponent pretty far when done)  
    - [ ] Gamble (flip a coin; if Bluee guesses correctly, Bluee gets a free hit, and if not, opponent gets a free hit)  
      * Ult Variant: Glorious & Gracious (Same thing, but now scales with half of the loser’s health)  
  - [ ] Weapon: Battle Blade of Bedlam

To Animate:

- [ ] Aidan’s Moveset  
  - [ ] M1 Chain  
    - [x] ~~Bare~~  
    - [ ] Weapon  
  - [ ] Bare Moves  
  - [ ] Weapon Moves  
- [ ] My Moveset  
  - [ ] M1 Chain  
    - [ ] Bare  
    - [ ] Weapon  
  - [ ] Bare Moves  
  - [ ] Weapon Moves  
- [ ] Zachary’s Moveset  
  - [ ] M1 Chain  
    - [ ] Bare  
    - [ ] Weapon  
  - [ ] Bare Moves  
  - [ ] Weapon Moves  
- [ ] Gabriel’s Moveset  
  - [ ] M1 Chain  
    - [ ] Bare  
    - [ ] Weapon  
  - [ ] Bare Moves  
  - [ ] Weapon Moves  
- [ ] Hit Animation (misc)