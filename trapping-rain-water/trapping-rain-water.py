class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeftHeight = [0] * len(height)
        for i in range(1, len(height)):
            maxLeftHeight[i] = max(maxLeftHeight[i-1], height[i-1])
        maxRightHeight = [0] * len(height)
        for i in range(len(height)-2,-1,-1):
            maxRightHeight[i] = max(maxRightHeight[i + 1], height[i+1])
        
        res = 0
        for i in range(len(height)):
            temp = (min(maxLeftHeight[i], maxRightHeight[i]) - height[i]) 
            res += temp if temp >= 0 else 0
        return res