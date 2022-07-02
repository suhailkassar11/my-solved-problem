class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n<3:
            return n
        left = 0
        right =1
        count = 0
        while(right < n):
            if nums[left] != nums[right]:
                left +=1
                nums[left] = nums[right]
                count = 0
            elif (nums[left] == nums[right] and count < 1):
                count +=1
                left +=1
                nums[left] = nums[right]
            right +=1
        return left+1