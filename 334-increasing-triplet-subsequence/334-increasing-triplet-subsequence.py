class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        fn = float("inf")
        sc = float("inf")
        
        for i in nums:
            if i <= fn:
                fn = i
            elif i <= sc:
                sc = i
            else:
                return True
        return False