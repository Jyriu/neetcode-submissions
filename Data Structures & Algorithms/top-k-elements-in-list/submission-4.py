from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        res = [n[0] for n in count.most_common()[:k]]

        return res        