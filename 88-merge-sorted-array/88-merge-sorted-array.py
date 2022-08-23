class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n==0:
            return nums1
        for i in range(len(nums2)):
            nums1[-1-i]=nums2[i]
        nums1.sort()
        return nums1