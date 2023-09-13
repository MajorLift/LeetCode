// https://leetcode.com/problems/min-stack




typedef struct {
    int allocSize;
    int* elems;
    int currSize;
    int* mins;
    int minSize;
} MinStack;

/** initialize your data structure here. */

MinStack* minStackCreate() {
    int initAllocSize = 4;
    MinStack* minStack = (MinStack*) malloc(sizeof(MinStack));
    minStack->elems = (int*) malloc(sizeof(int) * initAllocSize);
    minStack->currSize = 0;
    minStack->allocSize = initAllocSize;
    minStack->mins = (int*) malloc(sizeof(int) * initAllocSize);
    minStack->minSize = 0;
    return minStack;
}

int minStackGetMin(MinStack* obj) {
    return obj->mins[obj->minSize - 1];    
}

void minStackPush(MinStack* obj, int x) {
    if(obj->currSize == obj->allocSize){
        obj->allocSize *= 2;
        obj->elems = (int*) realloc(obj->elems, obj->allocSize);
        obj->mins = (int*) realloc(obj->mins, obj->allocSize);
    }
    obj->elems[obj->currSize++] = x;
    
    int min = minStackGetMin(obj);
    if(x < min){
        obj->mins[obj->minSize++] = x;
    }
    else obj->mins[obj->minSize++] = min;
}

int minStackTop(MinStack* obj) {
    return obj->elems[obj->currSize - 1];
}

void minStackPop(MinStack* obj) {
    if(obj->currSize > 0){
        --(obj->currSize);
        --(obj->minSize);
    }
}

void minStackFree(MinStack* obj) {
    free(obj->elems);
    free(obj->mins);
}

/**
 * Your MinStack struct will be instantiated and called as such:
 * MinStack* obj = minStackCreate();
 * minStackPush(obj, x);
 
 * minStackPop(obj);
 
 * int param_3 = minStackTop(obj);
 
 * int param_4 = minStackGetMin(obj);
 
 * minStackFree(obj);
*/