// https://leetcode.com/problems/contains-duplicate

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> mp;
        for (auto num : nums) mp[num]++;
        for (auto pair : mp) {
            if (pair.second > 1) return true;
        }
        return false;
    }
};