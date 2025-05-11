class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        '''
        1. check to see if duplicates exist, if so they are k apart 
        2. if present return True else False

        use a map and log an item and its index 
        '''

        mapp = {}

        for i, num in enumerate(nums):
            if num in mapp:
                if abs(i - mapp[num]) <= k:
                    return True
            mapp[num] = i
        return False
