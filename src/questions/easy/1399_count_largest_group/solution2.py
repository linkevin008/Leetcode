class Solution:
    def countLargestGroup(self, n: int) -> int:
        '''
        there is a pattern 
        order 0: 1 - 9
        order 1: 10 - 99
        order 2: 100 - 999

        we can resuse precomputed digit_sums of the same order and 
        just add in the reminader i.e. 11 = digit_sum(2) 

        but 15 = digit_sum(6) -> dp[10] + remainder

        have a dp for storing computed digitsums 

        and have an array for listing the frequency of occurence for a specific digitsum

        time complexity: O(n)
        space complexity: O(n)
        '''

        dp = [0] * (n + 1)

        max_digit_sum = 9 * len(str(n))
        freq = [0] * (max_digit_sum + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i // 10] + i % 10
            freq[dp[i]] += 1

        largest_count = max(freq)

        return freq.count(largest_count)
