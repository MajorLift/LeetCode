// https://leetcode.com/problems/subsets

class Solution {
    private List<List<Integer>> output;
    private int[] nums;

    public List<List<Integer>> subsets(int[] nums) {
        this.output = new ArrayList<>();
        this.nums = nums;
        backtrack(new ArrayList<>(), 0);
        return this.output;
    }

    private void backtrack(List<Integer> path, int start) {
        this.output.add(path);
        for (int i = start; i < this.nums.length; ++i) {
            List<Integer> newPath = new ArrayList<>(path);
            newPath.add(nums[i]);
            backtrack(newPath, i + 1);
        }
    }
    
}