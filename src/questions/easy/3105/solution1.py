class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:

        # O(n)

        # at each iteration check to see if the element prior is less than it

        # if less than increment count

        # if greater then reset update max_count if necessary

        prev = 0
        max_len = 0
        cur_len = 0

        for num in nums:
            if prev < num:
                cur_len += 1
            else:
                cur_len = 1
            max_len = max(max_len, cur_len)
            prev = num

        # do the same thing for the decreasing

        prev = 51
        cur_len = 0

        for num in nums:
            if prev > num:
                cur_len += 1
            else:
                cur_len = 1
            max_len = max(max_len, cur_len)
            prev = num
        return max_len