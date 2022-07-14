class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#         we cannot choose the max and min price and use them because the min could be before the max
# brute force : double for loops, check every subsequent day for every day and maintain a max profit so far - O(n**2) time space complexity
# sliding window approach : right = 1 + left 
# if rightVal - leftVal = -ve then update right and left pointers - right goes to where left was
# if rightVal - leftVal = +ve then update right pointer and max_profit
# O(n) time and O(1) space

        n = len(prices)
        if n < 2:
            return 0
        if n == 2 and prices[1] < prices[0]:
            return 0
        res = 0
        left, right = 0, 1
        while right < n:
            profit = prices[right] - prices[left]
            if profit < 0:
                left = right
                right = left + 1 
                continue
            
            res = max(res, profit)
            right += 1
        return res