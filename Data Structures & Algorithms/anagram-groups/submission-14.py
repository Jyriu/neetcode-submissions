class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()

        # store l'anagramme en clé + les strings en valeurs
        for s in strs:
            key = ''.join(sorted(s))
            if key in anagrams:
                anagrams[key] += [s]
            else:
                anagrams[key] = [s]


        # return les values du dict sous liste
        return list(anagrams.values())