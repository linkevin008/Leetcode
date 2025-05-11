class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:

        # Optimal Solution: O(n)

        # at each iteration check to see if the element prior is less than it

        # if less than increment count

        # if greater then reset update max_count if necessary

        prev = 0
        max_len = 0
        inc_cur_len = 0
        dec_cur_len = 0

        for num in nums:
            # incr
            if prev < num:
                inc_cur_len += 1
            else:
                inc_cur_len = 1

            # decr
            if prev > num:
                dec_cur_len += 1
            else:
                dec_cur_len = 1

            max_len = max(max_len, inc_cur_len, dec_cur_len)
            prev = num
        return max_len