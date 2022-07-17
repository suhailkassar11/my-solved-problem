class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        cout=0
        ind=0
        g.sort()
        s.sort()
        for greed in g:
            while(ind<len(s)):
                if greed<=s[ind]:
                    cout+=1
                    ind+=1
                    break
                ind+=1
        return cout
                