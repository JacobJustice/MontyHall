# MontyHall
A program that allows you to brute force the Monty Hall problem over any number of trials

# The Problem
The Monty Hall Problem is a brain teaser from the game show "Let's Make a Deal" and named after the host.

From Wikipedia:

"Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?"

# The Solution
Intuitively you would think that If you switch to the other door every time, you will have a 2/3 chance of winning the prize. The simplest explanation of this is assume you always switch, and the doors look like this:

{1:Prize, 2:Goat1, 3:Goat2}

This setup results in only 3 different types of situations. 

Situation 1: you unknowingly pick the car and the host reveals Goat1 (or Goat2) to you, you agree to switch and you get Goat2 (or Goat1). 

Situation 2: you unknowingly pick Goat1 and the host reveals Goat2 to you, you agree to switch and you get the car.

Situation 3: you unknowingly pick Goat2 and the host reveals Goat1 to you, you agree to switch and you get the car.

If you never switch, then you only have a 1/3 chance of winning as you only use your first choice.

# The Program
The program has various flags that give you full control of the problem.

Required flags:

-n or --number controls the number of times the program is run

Optional flags:

-m or --manual if on, allows you to play the game yourself n number of times

-g or --goat allows you to place the prize in that door every single time

-s or --switch if on, tells the automated player to switch every time

# Results

Aligning with the mathematical proof, every time the program is told to switch every time and run over a large number of iterations, the number of wins is roughly 66% or 2/3 of the time.
