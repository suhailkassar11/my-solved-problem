class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        from collections import Counter
        n = len(nums)
        count = Counter(nums)
        for key,value in count.items():
            if value > n//2:
                return key