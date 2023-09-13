// https://leetcode.com/problems/minimum-size-subarray-sum



int minSubArrayLen(int s, int* nums, int numsSize){
    if(numsSize == 0) return 0;
    int solSize = 1;
    while(solSize < numsSize){
        int i = 0;
        while(i < numsSize - solSize + 1){
            int j = 0;
            int sum = 0;
            while(j < solSize) sum += nums[i + (j++)];
            if(sum == s) break;
            i++;
        }
        if(i < numsSize - solSize + 1) break;
        solSize++;
    }
    if(solSize == numsSize) return 0;
    return solSize;
}

