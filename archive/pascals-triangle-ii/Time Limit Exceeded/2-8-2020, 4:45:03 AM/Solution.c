// https://leetcode.com/problems/pascals-triangle-ii



/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

// f(5, 3) = f(4, 2) + f(4, 3) = f(3, 1) + f(3, 2) + f(3, 2) + f(3, 3)
//          = 1 + f(2, 1) + f(2, 2) + f(2, 1) + f(2, 2) + 1
//          = 6

int recursivePascalCell(int i, int j){
    if(i == 0 || j == 0 || j == i){
        return 1;
    }
    int p = 0;
    p += recursivePascalCell(i-1, j-1) + recursivePascalCell(i-1, j);
    return p;
}

int* getRow(int rowIndex, int* returnSize){
    *returnSize = rowIndex + 1;
    int* q = (int*) malloc(*returnSize * sizeof(int));
    q[0] = 1;
    q[rowIndex] = 1;
    
    int j = 1;
    while(j < rowIndex){
        q[j] = recursivePascalCell(rowIndex, j);
        j += 1;
    }
    return q;
}

