from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            sorteds = ''.join(sorted(s))
            anagrams[sorteds].append(s)

        return list(anagrams.values())