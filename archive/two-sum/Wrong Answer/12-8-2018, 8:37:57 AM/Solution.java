// https://leetcode.com/problems/two-sum

class Solution {
    private static int[] result;
    public int[] twoSum(int[] nums, int target) {
        for (int i=0; i<nums.length; ++i) {
            int difference = target - nums[i];
            for (int j=i+1; j<nums.length; ++j) {
                if (nums[j] == difference) {
                    int[] result = {i,j};
                    break;
                }
            }
        }
        return result;
    }
}
