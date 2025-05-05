class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        '''
        find all possible subarrays of each string

        and check to see if they exist in others

        1. n^2 to find all substrings of a string
        2. insert into a map (substring : count) 
        3. iterate through again (sort) and see if the count is 1, if it is then take it else don't if at the end then ""

        '''

        count_map = Counter()

        subarray_map = dict() # index : set
        index = 0


        def get_substrs(s): 
            substrs = list()
            n = len(s)
            for i in range(n):
                for j in range(i, n):
                    substrs.append(s[i:j + 1])
            return set(substrs)

        def track_count(substrs):
            for substr in substrs:
                count_map[substr] += 1

        for s in arr:

            substrs = sorted(get_substrs(s), key = lambda x: (len(x), x))
            subarray_map[index] = substrs
            track_count(substrs)

            index += 1

        ans = []
        # print(subarray_map)

        for i in range(len(arr)):
            substrs = subarray_map[i]
            element = ""

            for s in substrs:
                if count_map[s] == 1:
                    element = s
                    break
            ans.append(element)

        return ans
