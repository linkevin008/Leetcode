class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        '''
        LCA -> using parents
        '''

        parent_mapp = dict()

        for region_list in regions:
            parent = region_list[0]

            for child in region_list[1:]:
                parent_mapp[child] = parent

        visited = set()
        r1 = region1
        r2 = region2
        while True:
            if r1:
                if r1 in visited:
                    return r1
                visited.add(r1)
                r1 = parent_mapp.get(r1)
            if r2:
                if r2 in visited:
                    return r2
                visited.add(r2)
                r2 = parent_mapp.get(r2)