# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self,head):
        if not head or not head.next :
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return new_head

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 
        slow = head 
        fast = head 
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next 
        
        second = self.reverseList(slow.next )
        slow.next = None
        first = head 

        while first and second:
            t1 = first.next
            t2 = second.next 
            first.next = second 
            second.next = t1

            first = t1 
            second = t2
       