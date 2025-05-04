class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        '''
        dfs:
            starting from Earth check to see if its children contain both regions 
            if only 1 child contains both then we can go deeper
            if both regions show up from separate children then this current region is the LCA

        '''
        # found_region1 = False
        # found_region2 = False
        # iteration

        mapp = defaultdict(list)

        for region_list in regions:
            for i in range(1, len(region_list)):
                mapp[region_list[0]].append(region_list[i])


        def is_region_in_area(region, parent):
            if parent == region:
                return True

            for neighbor in mapp[parent]:
                if region == neighbor:
                    return True
                else:
                    if is_region_in_area(region, neighbor):
                        return True
            return False


        ans = None
        for region_list in regions:
            cur_region = region_list[0]
            found_region1 = False
            found_region2 = False

            # check region1 and check region2
            if is_region_in_area(region1, cur_region):
                found_region1 = True
            if is_region_in_area(region2, cur_region):
                found_region2 = True

            if found_region1 and found_region2:
                ans = region_list[0]

        return ans
