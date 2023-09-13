// https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast, slow = head, head
        counter = 0
        
        while counter < n:
            fast = fast.next
            counter += 1
        
        while fast is not None:
            fast = fast.next
            slow = slow.next
            
        return slow
        