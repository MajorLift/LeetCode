// https://leetcode.com/problems/plus-one



/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* plusOne(int* digits, int digitsSize, int* returnSize){
    int i = 0;
    while(i < digitsSize){
        if(digits[i++] != 9) break;
    }
    if(i == digitsSize){
        int* ret = (int*) malloc(sizeof(int) * (digitsSize + 1));
        i = 0;
        while(i < digitsSize + 1) ret[i++] = 0;
        ret[0] = 1;
    }
    else{
        int* ret = (int*) malloc(sizeof(int) * digitsSize);
        i = 0;
        while(i < digitsSize) ret[i++] = 0;
        i = 0;
        while(++i <= digitsSize){
            ret[digitsSize - i] = digits[digitsSize - i];
            if(i == 1){
                ret[digitsSize - i] += 1;  
            } 
            if(i > 1 && ret[digitsSize - i + 1] >= 10){
                ret[digitsSize - i + 1] -= 10;
                ret[digitsSize - i] += 1;
            }
        }
    }
    return ret;    
}

 