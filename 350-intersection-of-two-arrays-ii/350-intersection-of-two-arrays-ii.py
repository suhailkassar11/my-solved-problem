class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1
        hashmap = {}
        for num in nums1:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        output = []
        for num in nums2:
            if num in hashmap and hashmap[num] >= 1:
                hashmap[num] -= 1
                output.append(num)
        return output