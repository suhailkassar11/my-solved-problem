class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_transactions = 2
        profit = [[0]*len(prices) for _ in range(max_transactions+1)]
        for tran_id in range(1, max_transactions+1):
            current_max = float('-inf') 
            for d in range(1, len(prices)):
                current_max = max(profit[tran_id-1][d-1]-prices[d-1], current_max)
                profit[tran_id][d] = max(profit[tran_id][d-1], prices[d] + current_max) 
        return profit[-1][-1]
        