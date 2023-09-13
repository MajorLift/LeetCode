// https://leetcode.com/problems/remove-nth-node-from-end-of-list

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
    let [prevNode, nAhead] = [head, head];
    if (n === 1) {
        head.next = null;
        head = null;
    } else {
        for (let i = 0; i < n; i += 1) nAhead = nAhead.next;
        while (nAhead.next) {
            prevNode = prevNode.next;
            nAhead = nAhead.next;
        }
        const currNode = prevNode.next;
        prevNode.next = prevNode.next.next;
        currNode.next = null;
    }
    return head;
};