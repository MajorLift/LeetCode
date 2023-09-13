// https://leetcode.com/problems/swap-nodes-in-pairs

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* swapPairs(struct ListNode* head){    
    struct ListNode* current = head;
    if(current != NULL && current->next != NULL){
        int tmp = current->val;
        current->val = current->next->val;
        current->next->val = tmp;
               
        current->next->next = swapPairs(current->next->next);
        return current;
    }
    else{
        return head;
    }
}

