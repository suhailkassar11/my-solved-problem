class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0
        for i in range(len(nums)):
            if i > reachable:
                return 0
            if reachable >= len(nums)-1:
                return 1
            if i + nums[i] > reachable:
                reachable = i+nums[i]
        return 0