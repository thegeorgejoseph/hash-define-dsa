# Dynamic Programming - min cost to climb the stairs to reach the final step
​
## Brute Force
​
> Start at the beginning (root node) and take 1 / 2 steps and pay the cost
> O(2^n) time
> You find the solution by choosing the path that is the least expensive.
> But this does not mean you take the least expensive option at every step because that can lead to unnecessary number of steps.
​
## Memoized Solution
​
> Cache the cost at every node visited and take the solution from dp
​
## Dynamic Programming
​
> Base case: when you are the end how much do you have to pay to reach the end? : 0
> When you are at n - 1 how much do you have to pay to reach the end? cost[n-1]
> When you are at n -2 how much do you have to pay to reach the end?
* cost[n-2] and then take two steps
> When you are at n - 3 => you will take
* min (cost at n - 2, cost at n - 1)
​
OPT(i) = Minimum cost through i when you start at 0
OPT(i) = min(OPT(i-2), OPT(i-1))
​