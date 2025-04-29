class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        '''
        two pointer:
        right pointer increment += 1 and keep searching until max element is located k times

        once satisfied then the possible subarrays are n - right
        
        then increment the left pointer, if the condition is broken then increment right again

        '''
        max_element = max(nums)
        n = len(nums)

        left, right = 0, 0
        k_found = 0
        ans = 0


        for right in range(len(nums)):
            # increment
            if nums[right] == max_element:
                k_found += 1

                # count remaining
                if k_found >= k:
                    ans += n - right

                    # icnrement left
                    while k_found >= k:
                        left += 1
                        if nums[left - 1] == max_element:
                            k_found -= 1

                        if k_found >= k:
                            ans += n - right
        return ans
