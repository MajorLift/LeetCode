// https://leetcode.com/problems/kth-largest-element-in-a-stream

class KthLargest {
private:
    int _k;
    priority_queue<int> pq;
public:
    KthLargest(int k, vector<int>& nums) {
        _k = k;
        for (const int& num : nums) add(num);
    }
    
    int add(int val) {
        pq.push(-val);
        while (pq.size() > _k) pq.pop();
        return -pq.top();
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */