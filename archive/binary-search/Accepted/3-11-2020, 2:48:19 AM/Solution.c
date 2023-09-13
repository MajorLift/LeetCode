// https://leetcode.com/problems/binary-search



int search(int* nums, int numsSize, int target){
    int curr = numsSize / 2;
    int left = 0;
    int right = numsSize - 1;
    while(right - left >= 0 && left >= 0 && right < numsSize){
        if(nums[curr] == target) return curr;
        if(nums[curr] > target) right = curr - 1;
        if(nums[curr] < target) left = curr + 1;
        curr = left + (right - left + 1) / 2;
    }
    return -1;
}

