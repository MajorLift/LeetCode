// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted



/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize){
    unsigned int i, j;
    *returnSize = 2;
    int* ret = (int*) malloc(sizeof(int) * (*returnSize));
    
    i = -1;
    while(++i < numbersSize && numbers[i] < target);
    
    while(--i > 0){
        j = -1;
        while(++j < i){
            if(numbers[j] + numbers[i] == target) break;
        }
        if(j < i) break;
    }
    
    ret[0] = j + 1;
    ret[1] = i + 1;
    return ret;
}

