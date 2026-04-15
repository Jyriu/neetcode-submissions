class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = ''

        for c in s:
            c = c.lower()
            if c.isalnum():
                cleaned_s += c
        
        return True if cleaned_s[::-1] == cleaned_s else False
        #