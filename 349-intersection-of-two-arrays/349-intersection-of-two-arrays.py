class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        t=[]
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                t.append(nums1[i])
        t1=set(t)
        return t1
                
        