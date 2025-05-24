"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        return a deep copy of the graph

        naiive approach

        iterate through once and create a deep copy of each node and storing the new ones in a map 
        where the mapping is node val : node object

        iterate through again but this time when we see what nodes are present we populate our nodes with objects from the map

        how do we iterate?

        staring from a node we for loop through the neighbors and each time we call a recurisve function to dfs again


        ''' 
        if not node:
            return None

        new_node_map = dict()

        def deep_clone(root):
            if root.val not in new_node_map:
                new_node_map[root.val] = Node(root.val)
            
            for neigh in root.neighbors:
                if neigh.val not in new_node_map:
                    deep_clone(neigh)

                new_node_map[root.val].neighbors.append(new_node_map[neigh.val])

        deep_clone(node)
        return new_node_map[node.val]