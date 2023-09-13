// https://leetcode.com/problems/minimum-size-subarray-sum



int minSubArrayLen(int s, int* nums, int numsSize){
    int solSize = 0;
    while(solSize < numsSize){
        int i = 0;
        while(i < numsSize - solSize + 1){
            int j = 0;
            int sum = 0;
            while(j < solSize) sum += nums[i + (j++)];
            if(sum >= s) break;
            i++;
        }
        if(i < numsSize - solSize + 1) break;
        solSize++;
    }
    if(solSize == numsSize) return 0;
    return solSize;
}

