class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        lst=[]
        half1=nums[:n]
        half2=nums[n:]
        for i in range(n):
            lst.append(half1[i])
            lst.append(half2[i])
        return lst