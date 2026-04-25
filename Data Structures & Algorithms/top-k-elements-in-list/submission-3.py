import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()

        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1

        heap = [(count[n], n) for n in count]

        heapq.heapify(heap)

        res = list()

        for n in range(len(count) - k):
            heapq.heappop(heap)
        
        return [item[1] for item in heap]