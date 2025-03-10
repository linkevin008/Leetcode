# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        given a singly linked list, swap every other nodes

        an in place swap would mean

        None -> 1 -> 2 -> 3 -> None

        prev.next = next
        next.next = cur
        prev = cur
        cur = next
        next = next.next

        prev.next = next
        next.next = 
        cur.next = 3.next
        

        we need multiple pointers one for our current node and one for the previous node

        we can perform a swap by 
        '''

        if not head or not head.next:
            return head

        prev = ListNode(-1)
        cur = head
        nxt = cur.next
        new_head = prev

        while nxt:

            prev.next = nxt
            cur.next = nxt.next
            nxt.next = cur

            prev = cur
            cur = cur.next

            if cur and cur.next:
                nxt = cur.next
            else:
                break

        return new_head.next
