class Solution(object):
    def coinChange(self, coins, amount):
        dp = [[0] * (amount+1) for _ in range(len(coins))]
        if amount == 0:
            return 0
        min_count = amount + 2
        for i in range(0,len(coins)):
            for j in range(1,amount+1):
                dp[i][j] = dp[i-1][j]
                if coins[i] == amount:
                    return 1
                if coins[i] == j:
                    dp[i][j] = 1
                if coins[i] < j:
                    tmp = dp[i][j - coins[i]] + 1 if dp[i][j - coins[i]] else dp[i][j]
                    if dp[i][j]:
                        dp[i][j] = min(tmp,dp[i][j])
                    else:
                        dp[i][j] = tmp
            min_count = min(min_count,dp[i][amount]) if dp[i][amount] else min_count
        return min_count if min_count < amount +2 else -1