from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        '''
        naiive approach:

        nested for loop to compare every possible combination 
            - concatenate 
            - check if palindrome
        time complexity: n^2 * k where k is the length of a concatenated word
        space complexity: O(n) -> for answer list else constant
        '''


        def is_palindrome(word):
            left = 0
            right = len(word) - 1

            while left < right:
                if word[left] != word[right]:
                    return False
                left += 1
                right -= 1

            return True

        ans = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                concat_word = words[i] + words[j]
                print(f'i: {i}')
                if is_palindrome(concat_word):
                    ans.append([i,j])
        return ans