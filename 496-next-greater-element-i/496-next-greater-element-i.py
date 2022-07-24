class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s2_index = {}
        for index, value in enumerate(nums2):
            s2_index[value] = index
        
        result = []
        for num1_index, iterator in enumerate(nums1):
            index = s2_index[iterator]
            
            if index == len(nums2):
                result.append(-1)   
                continue
            
            for inner in nums2[index+1:]:
                if inner > iterator:
                    result.append(inner)
                    break
            
            if len(result) != num1_index+1:
                result.append(-1)
                
                
        return result