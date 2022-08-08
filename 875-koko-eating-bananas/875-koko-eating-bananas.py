class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = max(piles)
        while left <= right:
            k = left + (right - left) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            if hours <= h:
                right = k - 1
                res = min(res, k)
            else:
                left = k + 1
    
        return res
    # [3,6,7,11]
    # hours = 11 and then the guards return 
    # clearly if she eats 11 bananas per hour then the number of hours is equal to the len(array)
    # but what if k < len(hour) then it wont work i think
    # 1 , 2, 3, 4, 5, 6, 7, 8,  9, 10, 11
    # select the mid value and calculate the hours
    # if the hours <= h then find a smaller value, else find a larger value