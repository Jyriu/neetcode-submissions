class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()

        for s in strs:
            key = ''.join(sorted(s))
            if key in anagrams:
                anagrams[key] += [s]
            else:
                anagrams[key] = [s]
            print(type(anagrams.values()))
        return list(anagrams.values())