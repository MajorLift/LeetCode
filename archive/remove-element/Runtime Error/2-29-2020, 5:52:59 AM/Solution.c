// https://leetcode.com/problems/remove-element

int removeElement(int* nums, int numsSize, int val){
    int i = 0;
    int j = 0;
    while(j < numsSize){
        while(nums[j] == val) j++;
        if(j >= numsSize) break;
        nums[i++] = nums[j++];
    }
    return i;
}

