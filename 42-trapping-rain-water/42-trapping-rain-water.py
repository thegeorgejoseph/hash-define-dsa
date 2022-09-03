class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * (len(height))
        print(prefix)
        p = 0
        for i in range(len(prefix)):
            prefix[i] = p
            p = max(p, height[i])
        suffix = [0] * (len(height))
        s = 0
        for i in range(len(height)-1,-1,-1):
            suffix[i] = s
            s = max(s, height[i])
        water = 0
        for i in range(len(height)):
            water += max(min(prefix[i], suffix[i]) - height[i],0)
        return water