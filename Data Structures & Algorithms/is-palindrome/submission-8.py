class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ''

        for c in s:
            c = c.lower()
            if c.isalnum():
                clean_s += c
        
        return True if clean_s[::-1] == clean_s else False