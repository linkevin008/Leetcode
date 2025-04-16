class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        '''
        first figure out which element is the most common

        then go through checking if the following condition is achieved
            left: occurrences > len(index) // 2
            right: total - occurrences > len(nums) - index // 2

        Space Complexity: O(n)
        Time Complexity: O(n)

        '''
        count_map = Counter(nums)
        majority_element = count_map.most_common(1)[0][0]
        majority_element_occurrences = count_map.most_common(1)[0][1]

        count = 0
        ans = -1

        for i, num in enumerate(nums):
            if num == majority_element:
                count += 1
            left = (i + 1) // 2
            right = (len(nums) - 1 - i) // 2
            if count > left and majority_element_occurrences - count > right:
                return i

        return ans

