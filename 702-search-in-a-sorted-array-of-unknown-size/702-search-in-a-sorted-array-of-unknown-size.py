# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        if reader.get(0) == target:
            return 0
        
        left, right = 0, 1
        while reader.get(right) < target:
            left = right #you are reducing the search space by doing this
            right <<= 1
        print(left, right)
        while left <= right:
            mid = left + ((right - left) >> 1)
            pivot = reader.get(mid)
            
            if target < pivot:
                right = mid - 1
            elif target > pivot:
                left = mid + 1
            else:
                return mid
        return -1
            