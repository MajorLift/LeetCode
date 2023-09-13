// https://leetcode.com/problems/pascals-triangle



/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** generate(int numRows, int* returnSize, int** returnColumnSizes){
    *returnSize = numRows;
    
    int** q = (int**) malloc(sizeof(int*) * numRows);    
    int i = 0;
    while(i < numRows){
        q[i] = (int*) malloc(sizeof(int) * (i+1));   //q[i]
        q[i][0] = 1;    //q[i][0]
        q[i][i] = 1;    //q[i][i]
        i += 1;
    }
    
    *returnColumnSizes = (int*) malloc(sizeof(int) * numRows);
    i = 0;
    while(i < numRows){
        returnColumnSizes[i] = i+1;
        i += 1;
    }
    
    i = 2;
    while(i < numRows){
        int j = 1;
        while(j < i){
            q[i][j] = q[i-1][j-1] + q[i-1][j];
            j += 1;
        }
        i += 1;
    }
    
    return q;
}

