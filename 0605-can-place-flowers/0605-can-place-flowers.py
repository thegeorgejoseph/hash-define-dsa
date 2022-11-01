class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i, num in enumerate(flowerbed):
            if num != 0: continue
            left_empty = (i == 0) or (flowerbed[i-1] != 1)
            right_empty = (i == len(flowerbed)-1) or (flowerbed[i + 1] != 1)
            if left_empty and right_empty:
                n -= 1
                flowerbed[i] = 1
            if n == 0:
                return True
        
        return True if n <= 0 else False