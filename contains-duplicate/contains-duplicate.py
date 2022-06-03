class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        pool=set()
        for i in range(len(nums)):
            if nums[i] not in pool:
                pool.add(nums[i])
            else:
                return True
        return False