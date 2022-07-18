class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n=len(num)
        stack=[]
        max_k=k
        for val in num:
            while stack and stack[-1]>val and k>0:
                stack.pop()
                k-=1
            stack.append(val)
        while len(stack)>n-max_k:
            stack.pop()
        return str(int("0"+"".join(stack)))
