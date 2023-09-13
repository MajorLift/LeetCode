// https://leetcode.com/problems/find-median-from-data-stream

class MedianFinder {
    private Queue<Integer> minHeap;
    private Queue<Integer> maxHeap;

    public MedianFinder() {
        this.minHeap = new PriorityQueue<>((a, b) -> a - b);
        this.maxHeap = new PriorityQueue<>((a, b) -> b - a);
    }
    
    public void addNum(int num) {
        if (this.minHeap.size() > this.maxHeap.size()) {
            this.minHeap.add(num);
            int top = this.minHeap.poll();
            this.maxHeap.add(top);
        } else {
            this.maxHeap.add(num);
            int top = this.maxHeap.poll();
            this.minHeap.add(top);
        }
    }
    
    public double findMedian() {
        if (this.minHeap.size() == this.maxHeap.size()) return (this.minHeap.peek() + this.maxHeap.peek()) / 2.0;
        return this.minHeap.peek() * 1.0;
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */