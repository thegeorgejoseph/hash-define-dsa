# Dynamic Programming - number of distinct ways to get something
​
Dynamic Programming is __atleast__ a cached solution of a terribly recursive algorithm. If you can find an iterative way to implement the same caching (sometimes without using all the space needed) then it is a true bottom up dynamic programming solution.
_
_ _
_ _ _
## Brute Force? Terrible Recursion
​
Think of DP questions as a tree, at every step we have two decisions to make. If we do not memoize it, due to the presence of unwanted computation we will end up with a time complexity of O(2^n)
​
​
## Memoized? Better Recursion
​
Caching, we can store the number of ways to reach something at that node and then use normal DFS then we will get it in O(n) O(n) time space complexity
​
## Bottom Up DP? Tabular
​
[0,1,2,3,4,5] -> here 5 is the base case because base case is the tail of the tree not the root.
How to define a base case?
​
> How many ways can we reach 5 starting at 5? 1