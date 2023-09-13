class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int ans = 0;
        unordered_map<int, int> freq;
        for (auto& num : nums) {
            if (freq.contains(num)) ans += freq[num]++;
            else freq.emplace(make_pair(num, 1));
        }
        return ans;
    }
};