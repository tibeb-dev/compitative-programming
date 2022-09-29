# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stk = []
        ans = ListNode()
        temp = ans
        
        while(head):
            stk.append(head.val)
            head = head.next
        if len(stk) == 1:
            return True
        right = len(stk) - 1
        for i in range(len(stk)//2):
            if stk[i] != stk[right]:
                return False
            right -= 1
        return True