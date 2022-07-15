class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # we need to sort the array by time
        # we look at it in reverse also
        
        cars = [[p,s] for p,s in zip(position, speed)]
        stack = collections.deque([])
        
        for p,s in sorted(cars)[::-1]:
            time = (target - p) / s
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # this is not a while loop, we are checking and merging at each step so only need to compare top two 
                stack.pop()
        return len(stack)
        
        