class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_calculator=0
        max_sum=float("-inf")
        for num in nums:
            sum_calculator+=num
            if sum_calculator>max_sum:
                max_sum=sum_calculator
            if sum_calculator<0:
                sum_calculator=0
        return max_sum