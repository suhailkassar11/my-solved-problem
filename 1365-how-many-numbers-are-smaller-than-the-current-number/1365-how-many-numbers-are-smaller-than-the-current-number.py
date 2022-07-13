class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            value=nums[i]
            cout=0
            for j in range(len(nums)):
                if nums[j]<value:
                    cout+=1
            ans.append(cout)
        return ans