// https://leetcode.com/problems/max-consecutive-ones



int findMaxConsecutiveOnes(int* nums, int numsSize){
    int max = 0;
    int curr = 0;
    int i = 0;
    while(i < numsSize){
        if(nums[i] == 1) curr++;
        else curr = 0;
        if(curr >= max) max = curr;
        i++;
    }
    return max;
}

