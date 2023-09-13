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
        this.output.add(new ArrayList<>(path));
        for (int i = start; i < this.nums.length; ++i) {
            path.add(nums[i]);
            backtrack(path, i + 1);
            path.remove(path.size() - 1);
        }
    }
    
}