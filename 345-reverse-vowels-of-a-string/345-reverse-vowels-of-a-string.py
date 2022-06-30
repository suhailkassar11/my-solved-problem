class Solution:
    def reverseVowels(self, s: str) -> str:
        i=0
        j=len(s)-1
        s=list(s)
        vowels=['a','e','i','o','u','A','E','I','O','U']
        while i<j:
            if s[i] in vowels:
                if s[j] in vowels:
                    temp=s[i]
                    s[i]=s[j]
                    s[j]=temp
                    j-=1
                    i+=1
                else:
                    j-=1
            else:
                i+=1
        return "".join(s)
            