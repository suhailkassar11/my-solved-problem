class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans=[]
        s=set(nums)
        for i in s:
            if nums.count(i)>len(nums)//3:
                ans.append(i)
        return ans
        