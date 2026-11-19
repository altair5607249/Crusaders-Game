# Dashing
This is the legendary tale of a single equation and the applied math, basic calculus, and systems thinking behind it.

## Motives in Math
I wanted to create an equation that would dictate a player character's displacement during a dash.

As easy as it would've been to find the equation I wanted online, I wanted to know if I was actually good at math. In my opinion, there's a huge difference between excelling at a standard curriculum and following your own path regarding math.

At the time, my battle with depression was finally calming down, so I thought it would be a good time to get back into the groove of math. After all, I really love math, despite what my performance in AP Precalculus indicated; I couldn't bring myself to pay attention to the lessons, nor do my homework, nor study, so creating this equation would be my apology to my teacher, to math, and to myself.

## Deriving the Equation
My main tool here was [Desmos](https://www.desmos.com/), since I needed to visualize the equation's graph without frying my brain.

At first, I started off by listing the constraints I needed the equation to account for: elapsed time, max velocity, and motion behavior. My base would be a negative parabola, but I needed to mold that parabola with these constraints in mind.

My first thought was to use a parametric equation, but I quickly realized that I did not know enough about them to put them to good use. After that, I tried throwing random things into Desmos to no avail; I was practically banging my head against a wall, waiting for an answer to grace me. Soon enough, half of an answer came to me, but it was just turning my guesses into something readable with basic algebraic manipulation.

Frankly, I didn't know what I was doing. I thought doing this would be easy, but it clearly wasn't since I was going off of pure intuition. You would think my solution to that would be to use actual mathematical processes, but it wasn't: I just reinforced my intuition with self-correction and pattern recognition.

I noticed that the dash should start at peak velocity and accelerate in the opposite direction over time, so I got rid of the horizontal shift (c) to prevent the equation from starting at its floor. After taking that away, I noticed that the velocity reached zero at the same value as the compression factor's (b) denominator, so I set it to the value I wanted... and it worked! The vertical translation (d) already accounted for the max velocity, and the parabola was the motion behavior I wanted, so this was the final piece of the puzzle. I'd done it.

$$v(t) = -(bt)^2 + d \quad \text{or more precisely} \quad v(t) = -\left(\frac{\sqrt{d}}{T}t\right)^2 + d \quad (\text{where } T = \text{total time})$$

The algebra checks out too. Starting at time (t) = 0, the first term would evaluate to 0, leaving only the vertical translation to decide the initial velocity. 

$$v(0) = -(b \cdot 0)^2 + d = d$$

Afterwards, the velocity decreases, reaching 0 once b's denominator is equal to our desired time. This works because setting up the boundary condition gives us this:

$$v(T) = -(bT)^2 + d = 0$$

Solving the equation for time gives us our compression factor.

$$(bT)^2 = d \implies bT = \sqrt{d} \implies b = \frac{\sqrt{d}}{T}$$

You can also see my work [here](https://github.com/altair5607249/Crusaders-Game/blob/main/docs/gallery/general/systems-engineering/2026-06-29-final-dash-derivation.md).

This is structurally a vertex-form quadratic, but defining the compression factor in terms of the vertical translation (aka the max velocity) and total time allows this to function as a parameterized family of curves. If you are not familiar with the definition of this phrase, it essentially refers to a set of curves sharing the same general algebraic form or geometric structure, where the specifications of each individual curve are determined by one or more parameters. For a more in-depth explanation, please refer to [Dr. Eric Schechter's work](https://math.vanderbilt.edu/schectex/courses/f11/198/supplements/CURVES.pdf). 

The irony here is that I ended up with a parametric equation, despite avoiding one under the pretense that I didn't understand such equations.

## Applying Anticheat
If you think this story ends with the derivation, then I'm sorry to disappoint you, because there's much more to it than that.

About a month later, I found myself in need of an anticheat to prevent hackers from utilizing unfair movement in combat. I couldn't track `walkspeed`, since continuous teleportation ignored that and was faster, so I focused the system on predicting displacement. 

This worked well for movement with constant velocity such as walking and running, but dashing doesn't have that. Not even its acceleration is constant, which is what makes the feel of the move so authentic when considering air resistance and other types of friction. If I wanted to calculate the dash's displacement without breaking the authentic nature of the move itself, I would have to use basic calculus.

Thankfully, I studied a bit of it during my freshman year in high school (two years prior), so I was good enough to recognize that all I needed to do was integrate the original equation $v(t) = -(bt)^2 + d$. Doing this took 5-10 minutes, and I ended up with this:

$$\int \left(-b^2 t^2 + d\right) dt = -\frac{b^2 t^3}{3} + dt$$

In the [anticheat](https://github.com/altair5607249/Crusaders-Game/blob/main/src/ServerScriptService/ModuleLoader/Managers/MovementManager/init.luau), I used this new formula (housed by `dashDisplacement`) with definite integration in `maxDashDistance` to track dashing movement across a tick window, subtracting the previous time from the current time: 

```lua
local curveDisplacement = dashDisplacement(b, d, curveXNow) - dashDisplacement(b, d, curveXPrev)
```

This is also factored in with latency, walking overflow, and padding to return a fair result:

```lua
local xPrev = math.clamp((check or initialTime) - initialTime, 0, maxServerWindow) 
local xNow = math.clamp(finalTime - initialTime, 0, maxServerWindow)
local curveXPrev = math.clamp(xPrev, 0, dashDur)
local curveXNow = math.clamp(xNow, 0, dashDur)

--...

return curveDisplacement + overflowDisplacement + padding
```

This taught me that there was more to the derivation than its dictation of the player character's motion; it was good at describing itself, though that's to be expected. What I *mean to say* is that it set me up for recognizing its true, oddly broad utility.

## Reusing the Derivation
While I was finishing the closed beta and preparing for the open beta, I wondered about how to cleanly calculate Red and Green's damage scaling.

It bothered me that I used so much guessing for their bare-style moves' calculations, and by this time, I was programming their weapon-style moves, so I decided to get experimental while programming them. As I metaphorically banged my head against a wall, I thought back to the time I was banging my head against a wall while thinking up an equation for dashing.

"Wait, why can't I just use the same equation?" I asked myself.

So I tried it with Red's second weapon move ([Supernova](https://github.com/altair5607249/Crusaders-Game/blob/main/src/ServerScriptService/ModuleLoader/OutputModules/Weapon_Server/CharModules/Redd/Move2/init.luau)), and after flipping the sign... it worked.

```lua
local function healthCurve(health: number, maxHealth: number, stat: number)
	local a = maxHealth
	local b = (stat^(1/2))/a
	return (b*health)^2 + stat
end

--...

local attackData = { --for the shockwave
  atkdur = duration * 0.3, --0.375s
	atkrad = 30,
	atktype = "light",
	dmg = healthCurve(deltaHealth, maxHealth, 20),
	ID = 2,
	noKB = true,
	noSound = true,
	origin = root,
  style = "Weapon"
}

--...

local attackData2 = { --for the slash itself
	atkdur = duration * 0.1, --0.125s
	atkrad = 8,
	atktype = "heavy",
	customSound = script.KnifeHit,
	dmg = healthCurve(deltaHealth, maxHealth, 50),
	ID = 2,
	origin = root,
	style = "Weapon"
}

```

"Holy ####, it worked!"

It was pretty exciting to figure out that I'd actually invented my own family of curves from scratch, specifically a parameterized family of quadratic curves. Math is magic, and that magic came from my own two hands; stuff like that is pretty exciting, isn't it?

Here's a screenshot as proof of my madness: [awesomeness](https://github.com/altair5607249/Crusaders-Game/blob/main/docs/gallery/general/systems-engineering/2026-08-29-reusing-dash-derivation.md).

I didn't replace all of the pre-existing moves' code (e.g., [Hero's Fist](https://github.com/altair5607249/Crusaders-Game/blob/main/src/ServerScriptService/ModuleLoader/OutputModules/Bare_Server/CharModules/Redd/Move2/init.luau)) with it, but I definitely used it for the newer moves.
