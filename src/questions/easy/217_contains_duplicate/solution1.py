class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        '''
        use a counter and return True if a counter value contains > 2
        else return False
        '''

        counter = Counter(nums)

        for count in counter.values():
            if count >= 2:
                return True

        return False