// https://leetcode.com/problems/product-of-array-except-self

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        int prefix_prod = 1;
        int suffix_prod = 1;

        vector<int> output(n, 1);
        for (int i = 0; i < n; ++i) {
            output[i] *= prefix_prod;
            output[n - (i + 1)] *= suffix_prod;
            prefix_prod *= nums[i];
            suffix_prod *= nums[n - (i + 1)];
        }
        return output;
    }
};