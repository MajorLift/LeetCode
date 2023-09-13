// https://leetcode.com/problems/remove-element

int removeElement(int* nums, int numsSize, int val){
    if(numsSize == 0) return 0;
    int i = 0;
    int j = 0;
    while(j < numsSize){
        while(nums[j] == val) j++;
        if(j >= numsSize) return i;
        else nums[i++] = nums[j++];
    }
    return --i;
}

