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
        approach 2 with no additional memory:
        from n//2 node onward reverse it 
        then iterate from 0 to n//2 and stitch into the list the reversed list
        '''

        # get to n//2
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse
        prev = None
        curr = slow

        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # stitch
        first = head
        second = prev

        while second.next:
            first.next, first = second, first.next

            second.next, second = first, second.next
