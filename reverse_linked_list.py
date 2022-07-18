# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        newhead = ListNode()
        temp = []
        while(head):
            temp.append(head.val)
            head = head.next

        
        temp.reverse()
        
        x = newhead
        for i in temp:
            x.next = ListNode(i)
            x = x.next
        return newhead.next