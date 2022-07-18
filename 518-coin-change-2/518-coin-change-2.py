class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(amount + 1):
                if coin + i < amount + 1:
                    dp[coin + i] += dp[i]
        return dp[amount]