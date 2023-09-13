// https://leetcode.com/problems/remove-element

int removeElement(int* nums, int numsSize, int val){
    int i = 0;
    int j = 0;
    while(j < numsSize){
        while(nums[j] == val && j < numsSize - 1) j++;
        nums[i++] = nums[j++];
    }
    return --i;
}

