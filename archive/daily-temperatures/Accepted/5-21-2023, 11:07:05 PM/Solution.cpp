// https://leetcode.com/problems/daily-temperatures

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> answer(n, 0);
        stack<int> stack;
        for (int curr = 0; curr < n; ++curr) {
            int currTemp = temperatures[curr];
            while (!stack.empty() && temperatures[stack.top()] < currTemp) {
                int& prev = stack.top();
                stack.pop();
                answer[prev] = curr - prev;
            }
            stack.emplace(curr);
        }        
        return answer;
    }
};