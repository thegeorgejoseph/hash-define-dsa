class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_array = []
        pre = 1
        for i in range(n):
            prefix_array.append(pre * nums[i])
            pre = prefix_array[-1]
        post_array = []
        post = 1
        for i in range(n-1,-1,-1):
            post_array.append(post * nums[i])
            post = post_array[-1]
        post_array.reverse()
        
        res = []
        for i in range(n):
            if i == 0:
                res.append(1 * post_array[i + 1])
            elif i == n - 1:
                res.append(1 * prefix_array[i-1])
            else:
                res.append(prefix_array[i-1] * post_array[ i + 1])
        return res
            