# Definition for singly-linked list.
# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        final = ListNode(0)
        finalL = final
        output = []
        while(head):
            output.append(head.val)
            head = head.next
        middle = len(output)//2
        output = output[middle:]
        for i in output:
            finalL.next = ListNode(i)
            finalL = finalL.next
        return final.next