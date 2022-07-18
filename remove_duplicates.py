# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        temp = res
        ans = []
        
        while(head):
            ans.append(head.val)
            head = head.next
        ans = set(ans)
        ans = list(ans)
        ans.sort()
        for i in ans:
            temp.next = ListNode(i)
            temp = temp.next
        return res.next
    
        
        
        
        
        
        
        
        
        
        
        