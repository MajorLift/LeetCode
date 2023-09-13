// https://leetcode.com/problems/two-sum

class Solution {
    private static int m, n;
    public int[] twoSum(int[] nums, int target) {
        for (int i=0; i<nums.length-1; ++i) {
            int difference = target - nums[i];
            for (int j=i+1; j<nums.length; ++j) {
                if (nums[j] == difference) {
                    m = i;
                    n = j;
                    break;
                }
            }
        }
        return new int[] {m,n};
    }
}