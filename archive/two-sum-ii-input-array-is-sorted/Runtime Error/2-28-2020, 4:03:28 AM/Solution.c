// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted



/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize){
    int i = -1;
    while(numbers[++i] < target && i < numbersSize);
    int j;
    while(--i > 0){
        j = -1;
        while(++j < i){
            if(numbers[j] + numbers[i] == target) break;
        }
        if(j < i) break;
    }
    *returnSize = 2;
    int* ret = (int*) malloc(sizeof(int) * (*returnSize));
    ret[0] = j + 1;
    ret[1] = i + 1;
    return ret;
}

