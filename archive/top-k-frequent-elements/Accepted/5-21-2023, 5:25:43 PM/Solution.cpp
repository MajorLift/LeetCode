// https://leetcode.com/problems/top-k-frequent-elements

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> map;
        for (const int& num : nums) {
            map[num]++;
        }
        vector<vector<int>> buckets(nums.size() + 1);
        for (const auto& p : map) {
            buckets[p.second].push_back(p.first);
        }
        vector<int> output;
        for (int i = buckets.size() - 1; i >= 0 && output.size() < k; --i) {
            for (const int& num : buckets[i]) {
                output.push_back(num);
                if (output.size() == k) break;
            }
        }
        return output;
    }
};