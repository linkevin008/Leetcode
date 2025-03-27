# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Idea:
        Since both are sorted we can have two pointers 1 on list1 and 1 on list2.
        Then we can iterate

        Case1: list1 <= list2 then we take list1 as the next pointer (ptr.next = list1)
        Case2: list1 > list2 then we take list2 as the next pointer (ptr.next = list2)


        Time Complexity: O(n + m) m = len(list1) n = len(list2)
        Space Complexity: O(1) - we are not creating any new structures, we are reusing existing ones
        '''


        new_head = ListNode(-1)
        ptr = new_head

        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    ptr.next = list1
                    list1 = list1.next
                else:
                    ptr.next = list2
                    list2 = list2.next

                ptr = ptr.next

            elif list1:
                ptr.next = list1
                break

            elif list2:
                ptr.next = list2
                break

        return new_head.next