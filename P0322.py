# Time: O(mn)
# Space: O(n)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[amount+1 for _ in range(amount+1)]
        dp[0]=0
        for i in range(1,amount+1):
            for coin in coins:
                if i>=coin:
                    dp[i]=min(dp[i],1+dp[i-coin])
        return dp[-1] if dp[-1]<amount+1 else -1
