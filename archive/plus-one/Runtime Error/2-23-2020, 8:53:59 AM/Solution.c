// https://leetcode.com/problems/plus-one



/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* plusOne(int* digits, int digitsSize, int* returnSize){
    int* ret;
    int i = 0;
    while(i < *returnSize){
        if(digits[i++] != 9) break;
    }
    if(i == *returnSize){
        ret = (int*) malloc(sizeof(int) * (*returnSize + 1));
        i = 0;
        while(i < *returnSize + 1) ret[i++] = 0;
        ret[0] = 1;
    }
    else{
        ret = (int*) malloc(sizeof(int) * *returnSize);
        i = 0;
        while(i < *returnSize) ret[i++] = 0;
        i = 0;
        while(++i <= *returnSize){
            ret[*returnSize - i] = digits[*returnSize - i];
            if(i == 1){
                ret[*returnSize - i] += 1;  
            } 
            if(i > 1 && ret[*returnSize - i + 1] >= 10){
                ret[*returnSize - i + 1] -= 10;
                ret[*returnSize - i] += 1;
            }
        }
    }
    return ret;    
}

 