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

`v(t) = -(bt)² + d`, or more precisely `v(t) = (√(d)/T)*t)² + d` where T = total time

The algebra checks out too. Starting at time (t) = 0, the first term would evaluate to 0, leaving only the vertical translation to decide the initial velocity. 

`v(0) = -(b*0)² + d = d`

Afterwards, the velocity decreases, reaching 0 once b's denominator is equal to our desired time. This works because setting up the boundary condition gives us this:

`v(T) = -(bT)² + d = 0`

Solving the equation for time gives us our compression factor.

`(bT)² = d` → `bT = √(d)` → `b = √(d)/T`

You can also see my work [here](https://github.com/altair5607249/Crusaders-Game/blob/main/docs/gallery/general/systems-engineering/2026-06-29-final-dash-derivation.md).

This is structurally a vertex-form quadratic, but defining the compression factor in terms of the vertical translation (aka the max velocity) and total time allows this to function as a parameterized family of curves. If you are not familiar with the definition of this phrase, it essentially refers to a set of curves sharing the same general algebraic form or geometric structure, where the specifications of each individual curve are determined by one or more parameters. For a more in-depth explanation, please refer to [Dr. Eric Schechter's work](https://math.vanderbilt.edu/schectex/courses/f11/198/supplements/CURVES.pdf). The irony here is that I ended up with a parametric equation, despite avoiding one under the pretense that I didn't understand such equations.

## Applying Anticheats
(TBC)
