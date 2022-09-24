class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                if abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                    break
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                    continue
                if abs(stack[-1]) > abs(asteroid):
                    break
            else:
                stack.append(asteroid)
        return stack
                    