// https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast, slow = head, head
        counter = 1
        
        while counter < n:
            if fast.next is None:
                return None
            fast = fast.next
            counter += 1
        
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        
        if slow == head:
            return slow.next
            
        skip_node = slow.next.next
        slow.next.next = None
        slow.next = skip_node
            
        return head
        