class Solution {
public:
    int differenceOfSum(vector<int>& nums) {
        int elem_sum = 0, digit_sum = 0;
        for (auto& num : nums) {
            elem_sum += num;
            for (auto& ch : to_string(num)) {
                digit_sum += ch - '0';
            }
        }
        return elem_sum - digit_sum;
    }
};