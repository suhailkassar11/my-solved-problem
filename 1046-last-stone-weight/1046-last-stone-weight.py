class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while stones:
            y=stones.pop()
            if not stones:
                return y
            x=stones.pop()
            if y>x:
                for i in range(len(stones)+1):
                    if i==len(stones) or stones[i]>(y-x):
                        stones.insert(i,y-x)
                        break
        return 0
            