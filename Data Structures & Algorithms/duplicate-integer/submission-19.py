class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # duplicates -> set

        return True if len(set(nums)) != len(nums) else False