// https://leetcode.com/problems/binary-search



int search(int* nums, int numsSize, int target){
    int curr = numsSize / 2 + numsSize % 2;
    int len =  curr / 2;
    while(len > 0){
        if(nums[curr] > target) curr -= len;
        if(nums[curr] < target) curr += len;
        if(nums[curr] == target) return curr;
        len /= 2;
    }
    return -1;
}

