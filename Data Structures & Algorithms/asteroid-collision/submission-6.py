class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack =[]

        for a in asteroids:
            alive = True
            while alive and stack and stack[-1] > 0 and a < 0:
                if stack[-1] == abs(a):
                    stack.pop()
                    alive = False
                elif stack[-1] > abs(a):
                    alive = False 
                else:
                    stack.pop()
                    alive = True
            if alive:
                stack.append(a)
        return stack