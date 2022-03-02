class Solution:
    def reverseString(self, s: List[str]) -> None:
        n=len(s)
        for i in range(0,len(s)//2):
            s[i],s[n-i-1]=s[n-i-1],s[i]
        return s
            
    """
        Do not return anything, modify s in-place instead.
        """
        