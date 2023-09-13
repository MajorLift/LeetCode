// https://leetcode.com/problems/valid-anagram

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;
        unordered_map<char, int> cnt_s;
        unordered_map<char, int> cnt_t;
        for (int i = 0; i < s.length(); ++i) {
            cnt_s[s[i]]++;
            cnt_t[t[i]]++;
        }
        for (const auto &pair : cnt_s) {
            if (pair.second != cnt_t[pair.first]) return false;
        }
        return true;
    }
};