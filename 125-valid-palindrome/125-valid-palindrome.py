class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2=""
        s1="".join(ch for ch in s if ch.isalnum())
        s2=s1.lower()
        return s2==s2[::-1]