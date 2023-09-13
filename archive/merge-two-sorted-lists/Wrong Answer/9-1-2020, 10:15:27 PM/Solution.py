// https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        small = l1
        large = l2
        
        head = l1
        if l1 and l2 and l1.val > l2.val:
            head = l2
        
        while small and large:
            if small.val > large.val:
                tmp = small
                small = large
                large = tmp
                
            if small.next:
                if small.next.val <= large.val:
                    small = small.next
                else:
                    tmp = large.next
                    large.next = small.next
                    small.next = large
                    large = tmp
                    small = small.next.next
            else:
                small.next = large
                break
                
        return head


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next