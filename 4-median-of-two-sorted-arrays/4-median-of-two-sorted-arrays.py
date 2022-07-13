class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in range(len(nums2)):
            ele=nums2[i]
            nums1.append(ele)
        nums1.sort()
        if len(nums1)%2!=0:
            mid=len(nums1)//2
            ans=nums1[mid]
            return float(ans)
        else:
            mid1=len(nums1)//2
            mid2=mid1-1
            ans=(nums1[mid1]+nums1[mid2])/2
            return ans
            