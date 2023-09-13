// https://leetcode.com/problems/top-k-frequent-elements

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> cnt;
        for (const int& num : nums) {
            ++cnt[num];
        }
        vector<pair<int, int>> p;
        for (auto it = cnt.begin(); it != cnt.end(); ++it) {
            p.emplace_back(make_pair(-(it->second), it->first));
        }
        nth_element(p.begin(), p.begin() + k - 1, p.end());
        vector<int> output;
        for (int i = 0; i < k; ++i) {
            output.emplace_back(p[i].second);
        }
        return output;
    }
};