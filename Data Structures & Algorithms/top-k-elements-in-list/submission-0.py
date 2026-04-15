class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
# 1. count freq num in nums
# 2. sort the freq array and pick the top k frequent elements 

        counter = dict()

        for n in nums:
            if n in counter:
                counter[n] += 1
            else:
                counter[n] = 1


        pairs = list(counter.items())

        pairs = sorted(pairs, key=lambda x: x[1], reverse=True)

        return [num for num, freq in pairs[:k]]