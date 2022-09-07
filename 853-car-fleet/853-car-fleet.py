class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:    
        cars = [[position[i],speed[i]] for i in range(len(position))]
        # we need to sort the cars by position but also remember the corresponding times
        stack = []
        
        for p, s in sorted(cars)[::-1]:
            # if we start the cars that are closest to the target and then insert newer cars that take less time then they will actually match the time of the slower car so we can just pop the quicker (new one that was added) one
            time = (target - p) / s
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # there will be at least one fleet with how the question has been set up
                stack.pop()
        
        return len(stack)