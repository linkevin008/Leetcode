class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        '''
        we need to have volume iterations
        
        at each iteration we need to evaluate where the water is going

        we deposit the water at k and then we see if there is run off
            runoff is where there are adjacent locations that are the same level as the current of heights[k]
            if there is equal we shift to that spot to search if the minimum height ends up being heights[k] then thats is where the drop ends up
            if there is higher that is a sign to stop searching that way

            if there is lower we do the whole thing again but at the location

        '''

        def search_left(index, min_height, min_index):
            if index < 0 or heights[index] > min_height:
                return min_index
            if heights[index] == min_height:
                return search_left(index - 1, min_height, min_index)
            if heights[index] < min_height:
                return search_left(index - 1, heights[index], index)

        def search_right(index, min_height, min_index):
            if index == len(heights) or heights[index] > min_height:
                return min_index
            if heights[index] == min_height:
                return search_right(index + 1, min_height, min_index)
            if heights[index] < min_height:
                return search_right(index + 1, heights[index], index)
            
        

        for i in range(volume):
            # starting at heights[start]
            # benchmark the current height and see if we can go left and right 

            starting_height = heights[k]

            left_search = search_left(k - 1, starting_height, k)
            right_search = search_right(k + 1, starting_height, k)

            left_index = -1 if left_search == k else left_search
            right_index = -1 if right_search == k else right_search

            if left_index != -1:
                heights[left_index] += 1
            elif right_index != -1:
                heights[right_index] += 1
            else:
                heights[k] += 1


        return heights