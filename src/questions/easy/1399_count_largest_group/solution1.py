class Solution:
    def countLargestGroup(self, n: int) -> int:
        '''
        naiive way iterate through from 1 to n and add to a defaultdict(list) depending on the sum of digits

        time complexity is O(n) 
        space complexity is O(n)

        
        '''


        sum_map = defaultdict(list)
        
        def sum_components(num):
            str_num = str(num)
            total = 0
            for digit in str_num:
                total +=  int(digit)
            return total
        for i in range(1, n + 1):
            # sum components
            component_sum = sum_components(i)
            sum_map[component_sum].append(i)

        # find the largest count 
        max_count = 0
        for value in sum_map.values():
            max_count = max(max_count, len(value))

        count = 0
        for value in sum_map.values():
            if len(value) == max_count:
                count += 1

        return count
