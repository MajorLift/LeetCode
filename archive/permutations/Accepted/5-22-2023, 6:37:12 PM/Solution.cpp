// https://leetcode.com/problems/permutations

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        _n = nums.size();
        backtrack(nums, 0);
        return output;
    }
private:
    vector<vector<int>> output;
    int _n;
    void backtrack(vector<int>& nums, int start) {
        if (start == _n - 1) {
            output.push_back(nums);
            return;
        }
        for (int i = start; i < _n; ++i) {
            swap(nums[start], nums[i]);
            backtrack(nums, start + 1);
            swap(nums[start], nums[i]);
        }
    }
};