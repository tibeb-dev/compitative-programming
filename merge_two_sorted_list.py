import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        final = ListNode()
        temp = final
        res = []
        
        while(list1 or list2):
            if list1:
                res.append(list1.val)
                list1 = list1.next
            if list2:
                res.append(list2.val)
                list2 = list2.next
        res.sort()
        
        for i in res:
            temp.next = ListNode(i)
            temp = temp.next
        return final.next
        
            