class Solution:
    def isPalindrome(self, s: str) -> bool:
        d = "".join(i.lower() for i in s if i.isalnum())
        return d[::-1] == d
