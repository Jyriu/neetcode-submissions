class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = list()

        result = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp, index = stack.pop(-1)
                cur_day = i - index
                result[index] = cur_day

            stack.append([t, i])

        return result