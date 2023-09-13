// https://leetcode.com/problems/find-pivot-index



int pivotIndex(int* nums, int numsSize){
    int sum_all = 0;
    int i = 0;
    while(i < numsSize){
        sum_all += nums[i++];
    }
    int sum_left = 0;
    int sum_right = 0;
    i = 1;
    while(i < numsSize - 1){
        sum_left += nums[i - 1];
        sum_right = sum_all - (sum_left + nums[i]);
        if(sum_left == sum_right) return i;
        i++;
    }
    return -1;
}

