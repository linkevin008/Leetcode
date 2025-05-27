 class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        some sort of modified binary search

        when we do binary search we need to check some conditions:

        1. if left < right then we can keep right = middle - 1
        2. if left > right then we did a rotate and the minimum is between them
        3. if nums[middle - 1] > nums[middle] then nums[middle] is the minimum value
        '''

        left = 0
        right = len(nums) - 1

        while left < right:
            middle = left + ((right - left) // 2)

            # note it has to be middle + 1 to avoid negative index searching
            if nums[middle] > nums[middle + 1]:
                return nums[middle + 1]
            elif nums[left] < nums[right]:
                right = middle - 1
            elif nums[left] > nums[right]:
                if nums[left] > nums[middle]:
                    right = middle
                elif nums[left] < nums[middle]:
                    left = middle + 1

        return nums[left]
