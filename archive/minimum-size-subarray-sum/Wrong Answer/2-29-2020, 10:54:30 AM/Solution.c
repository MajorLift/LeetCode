// https://leetcode.com/problems/minimum-size-subarray-sum

int findMaxIndex(int* nums, int numsSize){
    int maxVal = 0;
    int maxIdx = -1;
    int i = -1;
    while(++i < numsSize){
        if(nums[i] > maxVal){
            maxVal = nums[i];
            maxIdx = i;
        }     
    }
    return maxIdx;
}
    

int minSubArrayLen(int s, int* nums, int numsSize){
    if(numsSize == 0) return 0;
    int maxIdx = findMaxIndex(nums, numsSize);
    int solSize = 1;
    while(solSize <= maxIdx + 1 || \
          solSize <= numsSize - maxIdx){
        int i = maxIdx - solSize + 1;
        if(i < 0) i = 0;
        while(i <= maxIdx && \
              i + solSize <= numsSize){
            int j = 0;
            int sum = 0;
            while(j < solSize) sum += nums[i + (j++)]; 
            if(sum >= s) break;
            i++;
        }
        if(i <= maxIdx && \
           i + solSize <= numsSize) break;
        solSize++;
    }
    if(solSize > maxIdx + 1 && \
       solSize > numsSize - maxIdx) return 0;
    return solSize;
}

