class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = dict()

        for i, j in enumerate(nums):
            diff = target - j
            if diff in store:
                return [store[diff], i]
            store[j] = i