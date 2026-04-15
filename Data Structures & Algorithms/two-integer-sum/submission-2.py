class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        viewed = dict()

        for i, n in enumerate(nums):
            diff = target - n

            if diff in viewed:
                return [viewed[diff], i]
            viewed[n] = i