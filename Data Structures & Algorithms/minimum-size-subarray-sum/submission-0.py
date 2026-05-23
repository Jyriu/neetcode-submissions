class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = window_sum = 0
        res = float('inf')

        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target: # as long as window is valid we shrink cuz all numbers positive, then every other bigger window will not be better solution
                res = min(res, right - left + 1)
                window_sum -= nums[left]
                left += 1
            
        return 0 if res == float('inf') else res