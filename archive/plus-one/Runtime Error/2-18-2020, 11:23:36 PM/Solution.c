// https://leetcode.com/problems/plus-one



/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* plusOne(int* digits, int digitsSize, int* returnSize){  
    *returnSize = digitsSize + 1;
    int* ret = (int*) malloc(sizeof(int) * (*returnSize));
    int i = 1;
    while(i <= digitsSize){
        ret[*returnSize - i] = digits[digitsSize - i];
        if(i == 1){
            ret[digitsSize - i] += 1;  
        } 
        if(i > 1 && ret[digitsSize - i + 1] >= 10){
            ret[*returnSize - i + 1] -= 10;
            ret[*returnSize - i] += 1;
        }
        if(i == digitsSize && ret[1] >= 10){
            ret[0] = 1;  
        } 
        else{
            *ret = *(ret + 1);
            *returnSize -= 1;
        } 
        i++;
    }
    return ret;
}

