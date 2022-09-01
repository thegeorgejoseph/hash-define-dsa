class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0:
            return False
        target = total // 3
        curSum, count = 0, 0
        for i in range(len(arr)):
            curSum += arr[i]
            if curSum == target:
                count += 1
                curSum = 0
        print(count)
        return True if count >= 3 else False