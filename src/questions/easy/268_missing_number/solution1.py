class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        naiive approach:
        1. sort the list
        2. then iterate through the numbers 0 to n seeing if they are present in the list

        time complexity:
        sort - O(nlogn)
        iterate - O(n)


        '''
        nums.sort(key = lambda x: (x))

        n = len(nums)
        for i, num in enumerate(nums):
            if num != i:
                return i

        return n