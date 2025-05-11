class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        '''
        approach 1:
        

        there are an odd number of consequtive 0s
            cannot put the flower on the sides
            n -= (num of consequtive 0s - 2) // 2
        there are an even number of consequetive 0s 
            n -= (num of consequtive 0s - 1)

        0 0 0 0 0 0 0 0 0 - ceil((9 - 2) / 2) 
        '''

        idx = 0

        while idx < len(flowerbed):
            if flowerbed[idx] == 0:
                search_ahead = idx
                # count cons 0s
                consequtive_zeroes = 0
                while search_ahead < len(flowerbed) and flowerbed[search_ahead] == 0:
                    consequtive_zeroes += 1
                    search_ahead += 1

                left = right = 1
                if idx == 0:
                    left = 0
                if search_ahead == len(flowerbed):
                    right = 0
                n -= math.ceil((consequtive_zeroes - (left + right)) / 2)
                # print(idx)
                idx = search_ahead
            else:
                idx += 1
        return n <= 0
