class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#         we cannot choose the max and min price and use them because the min could be before the max
# brute force : double for loops, check every subsequent day for every day and maintain a max profit so far - O(n**2) time space complexity
# sliding window approach : right = 1 + left 
# if rightVal - leftVal = -ve then update right and left pointers - right goes to where left was
# if rightVal - leftVal = +ve then update right pointer and max_profit
# O(n) time and O(1) space

        left, right = 0, 1
        n = len(prices)
        max_profit = 0
        while right < n : 
            if prices[left] > prices[right]:
                left = right
            else:
                max_profit = max(max_profit,prices[right] - prices[left])
                
            right += 1
            
        return max_profit
        