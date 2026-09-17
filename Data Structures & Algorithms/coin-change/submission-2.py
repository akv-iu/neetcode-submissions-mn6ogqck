class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [amount + 1] *(amount+1)
        dp[0] = 0

        for amnt in range(1,amount+1):
            for coin in coins:
                remaining = amnt - coin

                if remaining >= 0:
                    dp[amnt] = min(1+ dp[remaining], dp[amnt])
        
        return dp[amount] if dp[amount] < amount+1 else -1
        