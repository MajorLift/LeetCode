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
            this.minHeap.offer(num);
            this.maxHeap.offer(this.minHeap.poll());
        } else {
            this.maxHeap.offer(num);
            this.minHeap.offer(this.maxHeap.poll());
        }
    }
    
    public double findMedian() {
        if (this.minHeap.size() > this.maxHeap.size()) return this.minHeap.peek();
        return (this.minHeap.peek() + this.maxHeap.peek()) / 2.0;
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */