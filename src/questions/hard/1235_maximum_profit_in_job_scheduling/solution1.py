class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        '''
        sort on end time

        iterate through 

        using a heap with store the jobs and their profits as we go along

        we pop them off the heap when they don't conflict so that we can consider them

        we then append the nwe job to the heap using the max_profit + profit
        '''


        heap = []
        jobs = sorted(zip(startTime, endTime, profit), key = lambda x: x[0])
        max_profit = 0
        for start, end, p in jobs:

            while heap and heap[0][0] <= start:
                _, acc = heappop(heap)
                max_profit = max(max_profit, acc)
            
            heappush(heap, (end, max_profit + p))

        while heap:
            _, acc = heappop(heap)
            max_profit = max(max_profit, acc)

        return max_profit