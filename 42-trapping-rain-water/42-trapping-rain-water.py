class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        res = 0
        left, right = 0, len(height) - 1
        
        leftMaxHeight, rightMaxHeight = height[left], height[right]
        
        while left < right:
            if leftMaxHeight <= rightMaxHeight:
                left += 1
                temp = leftMaxHeight - height[left] if leftMaxHeight - height[left] >= 0 else 0
                res += temp
                leftMaxHeight = max(leftMaxHeight, height[left])
            else:
                right -= 1
                temp = rightMaxHeight - height[right] if rightMaxHeight - height[right] >= 0 else 0
                res += temp
                rightMaxHeight = max(rightMaxHeight, height[right])
        return res
    
#         nums= height
#         prefix = [i for i in height]
        
#         for i in range(1,len(height)):
#             prefix[i] = max(prefix[i-1], nums[i-1])
        
#         suffix = [i for i in height]
        
#         for i in range(len(height) - 2, -1, -1):
#             suffix[i] = max(suffix[i+1], nums[i+1])
        
#         res = [0] * (len(height) )
        
#         for i in range(len(height)):
#             temp = min(prefix[i], suffix[i]) - nums[i]
#             res[i] = temp if temp >= 0 else 0
        
#         return sum(res)