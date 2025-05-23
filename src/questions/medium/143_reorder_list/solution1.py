# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        '''
        naiive approach:
        iterate through while storing the index (say 0 to n) and mapping it index : node

        iterate thorugh again, but for n/2 times and reassign i.next to be n/2 + i

        MEMORY LIMIT EXCEEDED
        '''


        idx_to_node_map = dict()

        ptr = head
        idx = 0
        while ptr:
            idx_to_node_map[idx] = ptr
            idx += 1
            ptr = ptr.next

        n = len(idx_to_node_map)
        iterations = n // 2
        front_node = back_node = prev_back_node = None

        for i in range(iterations):
            print(i)
            front_node = idx_to_node_map[i]
            back_node = idx_to_node_map[n - i - 1]

            front_node.next = back_node
            if prev_back_node:
                prev_back_node.next = front_node
            prev_back_node = back_node

        if n % 2 == 1:
            prev_back_node.next = idx_to_node_map[iterations + 1]