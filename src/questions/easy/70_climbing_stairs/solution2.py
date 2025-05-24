class Solution:
    def climbStairs(self, n: int) -> int:
        '''

        dp approach

        iterate from 0 to n track how many ways we can get to arr[i]

        arr[i] = arr[i - 1] + arr[i - 2]

        time complexity O(n)
        space complexity O(n)
        '''

        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [0 for i in range(n + 1)]
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
