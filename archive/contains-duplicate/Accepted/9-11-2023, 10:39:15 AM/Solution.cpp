// https://leetcode.com/problems/contains-duplicate

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        return set(nums.begin(), nums.end()).size() < nums.size();
    }
};