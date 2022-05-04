class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        cout=0
        nums.sort()
        i=0
        j=len(nums)-1
        while i<j:
            if nums[i]+nums[j]>k:
                j-=1
            elif nums[i]+nums[j]<k:
                i+=1
            elif nums[i]+nums[j]==k:
                cout+=1
                j-=1
                i+=1
        return cout
            