class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''

        for c in s:
            c = c.lower()
            if c.isalnum():
                cleaned += c
                print(c)

        return True if cleaned[::-1] == cleaned else False