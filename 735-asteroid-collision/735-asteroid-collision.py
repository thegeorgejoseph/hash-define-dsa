class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                if abs(asteroid) == abs(stack[-1]):
                    stack.pop()
                    break
                if abs(asteroid) > abs(stack[-1]):
                    stack.pop()
                    continue
                if abs(asteroid) < abs(stack[-1]):
                    break
            else:
                stack.append(asteroid)
        return stack