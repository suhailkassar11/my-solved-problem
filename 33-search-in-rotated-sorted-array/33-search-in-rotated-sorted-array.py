class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return "-1"
        for i in  range(0,len(nums)):
            if nums[i]==target:
                return i
            
        