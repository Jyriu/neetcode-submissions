class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # lenght of strings ? if len != return false

        # if len(s) != len(t):
        #     return False

        # char order doesn't matter, sort both strings, if == then return true

        if Counter(s) == Counter(t):
            return True
        return False