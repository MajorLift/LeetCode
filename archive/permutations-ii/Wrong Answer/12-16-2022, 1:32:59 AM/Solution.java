// https://leetcode.com/problems/permutations-ii

class Solution {
    private final List<List<Integer>> output = new ArrayList<>();
    private int[] input;

    public List<List<Integer>> permuteUnique(int[] nums) {
        this.input = nums;
        Arrays.sort(this.input);
        backtrack(0);
        return this.output;
    }

    private void backtrack(int start) {
        if (start == this.input.length) {
            List<Integer> permutation = new ArrayList<>();
            for (int num : this.input) permutation.add(num);
            this.output.add(permutation);
            return;
        }
        for (int i = start; i < this.input.length; ++i) {
            if (i > start && this.input[i] == this.input[i - 1]) continue;
            swap(start, i);
            backtrack(start + 1);
            swap(start, i);
        }
    }

    private void swap(int i, int j) {
        int tmp = this.input[i];
        this.input[i] = this.input[j];
        this.input[j] = tmp;
    }
}