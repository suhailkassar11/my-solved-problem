class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        if target>nums[n-1]:
            return n
        elif target<nums[0]:
            return "0"
        for i in range(0,n):
            if target>nums[i] and target<nums[i+1]:
                return i+1
            elif target==nums[i]:
                return i
            
        