# Problem : Asteroid Collision
# Topic : Stack

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            alive = True
            while stack and stack[-1] > 0 and i < 0:
                if stack[-1] < abs(i):
                    stack.pop(-1)
                    continue
                if stack[-1] == abs(i):
                    stack.pop(-1)
                    alive = False
                    break
                if stack[-1] > abs(i):
                    alive = False
                    break
            if alive:
                stack.append(i)
        return stack                     
