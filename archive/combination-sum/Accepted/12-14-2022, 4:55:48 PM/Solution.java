// https://leetcode.com/problems/combination-sum

class Solution {
    private List<List<Integer>> output = new ArrayList<>();
    private int[] input;
    private int target;
    
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        this.input = candidates;
        this.target = target;
        backtrack(new ArrayList<>(), 0, this.target);
        return this.output;
    }

    private void backtrack(List<Integer> path, int start, int remainder) {
        if (remainder == 0) {
            this.output.add(new ArrayList<>(path));
            return;
        }
        for (int i = start; i < this.input.length; ++i) {
            if (remainder - this.input[i] >= 0) {
                path.add(this.input[i]);
                backtrack(path, i, remainder - this.input[i]);
                path.remove(path.size() - 1);
            }
        }
    }
}