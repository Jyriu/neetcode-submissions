class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_sum = l = 0
        res = float('inf')
        
        for r in range(len(nums)):
            window_sum += nums[r]
            while window_sum >= target:
                res = min(res, r - l + 1)
                window_sum -= nums[l]
                l += 1

        return 0 if res == float('inf') else res