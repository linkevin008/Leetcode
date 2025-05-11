class Solution:
    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        '''
        word1 + word2 

        if word1 is a palindrome then word2 has to be it but reversed  note; same length

        if word1 > word2 
            and word1 contains a palindrome then word2 could be word1 - palindrome in reverse

        if word1 < word2
            then vice versa
        '''

        def valid_prefix(word):
            valid_prefixes = list()
            # find the substring where it is a palindrome then return the remaining sequence
            for i in range(len(word)):
                if word[i:] == word[i:][::-1]:
                    valid_prefixes.append(word[:i])

            return valid_prefixes

        def valid_suffix(word):
            valid_suffixes = list()
            # find the substring where it is a palindrome then return the remaining sequence
            for i in range(len(word)):
                if word[:i+1] == word[:i+1][::-1]:
                    valid_suffixes.append(word[i + 1:])

            return valid_suffixes

        mapp = dict()
        ans = list()

        for i, word in enumerate(words):
            mapp[word] = i

        for i, word in enumerate(words):
            # equal case
            reversed_word = word[::-1]
            if reversed_word in mapp and i != mapp[reversed_word]:
                ans.append((i, mapp[reversed_word]))

            # word1 > word2
            valid_prefixes = valid_prefix(word)
            for prefix in valid_prefixes:
                reversed_prefix = prefix[::-1]
                if reversed_prefix in mapp:
                    ans.append((i, mapp[reversed_prefix]))

            # word1 < word2
            valid_suffixes = valid_suffix(word)
            for suffix in valid_suffixes:
                reversed_suffix = suffix[::-1]
                if reversed_suffix in mapp:
                    ans.append((mapp[reversed_suffix], i))

        return ans
