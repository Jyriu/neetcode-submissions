class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]

        cars = sorted(cars, reverse=True)

        stack = list()

        for p, s in cars:
            time = (target - p) / s
            stack.append(time)

            if len(stack) >= 2 and time <= stack[-2]:
                stack.pop(-1)
        
        return len(stack)