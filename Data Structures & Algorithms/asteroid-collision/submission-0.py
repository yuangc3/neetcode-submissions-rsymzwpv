class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for n in asteroids:

            while stack and stack[-1] > 0 and n < 0:
                if stack[-1] < abs(n):
                    stack.pop()
                    continue

                elif stack[-1] == abs(n):
                    stack.pop()

                # n 被撞碎，或者两者都碎了
                break

            else:
                stack.append(n)

        return stack