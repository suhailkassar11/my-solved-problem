class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        element_count={}
        for i in nums:
            if i in element_count:
                element_count[i]+=1
            else:
                element_count[i]=1
        for key,value in element_count.items():
            if value>1:
                return key