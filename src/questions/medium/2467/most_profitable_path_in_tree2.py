class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        '''
        build an adjacency matrix of the paths

        from bob's perspective, go towards the 0 root

        and while going log which day it took bob to get to that node

        bob's path: row -> day col -> root

        now we do a similar thing with alice but each time we visit a node we check to see if bob was
        at this node at the same time if so then we can either split the charge or split the profits amount/2
        or if bob visited this place sooner then we don't get the amount

        '''

        adj_matrix = defaultdict(list)

        for a, b in edges:
            adj_matrix[a].append(b)
            adj_matrix[b].append(a)

        n = len(amount)
        bob_template = [-1 for i in range(n)]
        bob_path = None

        def bob_walk(root, day, path, visited = set()):
            nonlocal bob_path
            visited.add(root)
            path[root] = day
            if root == 0:
                bob_path = path
                return 
            else:
                for neigh in adj_matrix[root]:
                    if neigh not in visited:
                        bob_walk(neigh, day + 1, list(path), visited)

        bob_walk(bob, 0, bob_template)

        ans = []
        def alice_walk(root, acc, day, visited = set()):
            visited.add(root)
            if bob_path[root] == -1:
                acc += amount[root]
            else:
                if bob_path[root] > day:
                    acc += amount[root]
                elif bob_path[root] == day:
                    acc += amount[root] / 2

            did_visit = False
            for neigh in adj_matrix[root]:
                if neigh not in visited:
                    alice_walk(neigh, acc, day + 1, visited)
                    did_visit = True

            if not did_visit:
                ans.append(acc)

        alice_walk(0, 0, 0)
        return int(max(ans))