class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_area = 0 # to return
        l, r = 0, len(heights) - 1

        while l <= r:
            # area = height * width(r - l)

            cur_area = min(heights[l], heights[r]) * (r - l)

            max_area = max(cur_area, max_area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_area