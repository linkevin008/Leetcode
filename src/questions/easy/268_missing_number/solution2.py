class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        '''
        1. create an arr of n items and set them to -1
        2. itereate through the nums and set the element at the index to be 1 or something else
        3. at the end check to see which index is still -1


        '''
        n = len(nums)
        arr = [-1 for i in range(n + 1)]
        
        for num in nums:
            arr[num] = 1

        return arr.index(-1)