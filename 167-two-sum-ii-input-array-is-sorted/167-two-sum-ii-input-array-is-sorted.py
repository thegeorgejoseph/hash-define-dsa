class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        if n == 2:
            return [1, 2] if numbers[0] + numbers[1] == target else [-1,-1]
        
        left = 0
        right = n - 1
        while left < right :
            if numbers[left] + numbers[right] == target:
                return [left + 1,right + 1]
            if numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        return [-1,-1]