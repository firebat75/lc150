class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal = ""
        for char in s:
            if char.isalnum():
                pal += char.lower()

        if pal == pal[::-1]:
            return True
        return False