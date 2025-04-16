class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        '''

        Using two pointers we attempt to go right from a given left until we find a good
        subarray because any subarray after that will be a good subarray so we can incr
        an ans count

        when iterating to the right we increment the number of seen pairs 
        by the count of the elements but we only increase the count after incrementing
        the pairs 

        iow we are evaluating the count at the time of evaluating the element but with in mind
        that we have previously incremented the count from a previous iteration

        Space Complexity: O(n) where n is the number of elements in the array
        Time Complexity: 
            iterate left n times and move right n times once
            => n
        '''
        n = len(nums)
        same, right = 0, -1
        cnt = Counter()
        ans = 0
        for left in range(n):
            while same < k and right + 1 < n:
                right += 1
                same += cnt[nums[right]]
                cnt[nums[right]] += 1
            if same >= k:
                ans += n - right
            cnt[nums[left]] -= 1
            same -= cnt[nums[left]]
        return ans


