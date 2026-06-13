class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        left = 0
        currentSum = 0


        for right in range(len(arr)):
            currentSum += arr[right]

            if right - left + 1 > k:
                currentSum -= arr[left]
                left += 1
            if currentSum >= threshold * k and right - left + 1 == k:
                count += 1
            
        
        return count