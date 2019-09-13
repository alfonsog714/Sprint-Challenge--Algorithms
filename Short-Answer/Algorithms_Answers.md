#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) The run time for this problem is O(n). There's only one iteration it runs through, being the `while` loop.

b) The run time for this problem is O(n^2). It runs through two iterations, the `for` loop initially and then the `while` loop.

c) This is a recursive function with the run time of O(2 + n!).

## Exercise II

Notes for self ---
n = total number of floors
f = floor number where eggs begin to break

GOAL: Determine the value of F so that the number of dropped + broken eggs is as small as possible

Keep track of the floor we're currently on.
Keep track of how many eggs have been dropped so far.
Keep note of whether or not an egg has broken yet or not, so maybe have a variable like "has_broken = False".
Loop over all the floors, going up higher and higher in the building.
Make a conditional loop, like a while loop. This will run as long as the has_broken variable is false.
At each floor, drop an egg.
If the egg didn't break, increment the number of eggs dropped so far. Also increment the floor we're on.
If the egg did break, increment the number of eggs dropped so far and set has_broken to True. Increment the floor we're on.

Return the floor that the while loop exited on.

The runtime complexity for this would be O(n^2) because it runs through two iterations, the `for` loop and the `while` loop.
