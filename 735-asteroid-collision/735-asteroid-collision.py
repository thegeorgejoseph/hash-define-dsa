class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for rock in asteroids:
            while stack and rock < 0 and stack[-1] > 0:
                if abs(stack[-1]) == abs(rock):
                    stack.pop()
                    break
                if abs(stack[-1]) < abs(rock):
                    stack.pop()
                    continue
                if abs(stack[-1]) > abs(rock):
                    break
            else:
                stack.append(rock)
        return stack
                