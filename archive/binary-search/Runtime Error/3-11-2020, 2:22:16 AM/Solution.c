// https://leetcode.com/problems/binary-search



int search(int* nums, int numsSize, int target){
    int curr = numsSize / 2;
    int len =  curr + 1;
    while(len > 0){
        len /= 2;
        if(nums[curr] > target) curr -= len;
        if(nums[curr] < target) curr += len;
        if(nums[curr] == target) return curr;
    }
    return -1;
}

