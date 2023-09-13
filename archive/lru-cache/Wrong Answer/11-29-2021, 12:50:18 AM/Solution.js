// https://leetcode.com/problems/lru-cache

/**
 * @param {number} capacity
 */
var LRUCache = function(capacity) {
    this.obj = {};
    this.counter = 0;
    this.capacity = capacity;
};

/** 
 * @param {number} key
 * @return {number}
 */
LRUCache.prototype.get = function(key) {
    if (!this.obj.hasOwnProperty(key)) return -1;
    const [value, _] = this.obj[key];
    this.obj[key][1] = ++this.counter;
    return value;
};

/** 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
LRUCache.prototype.put = function(key, value) {
    if (Object.keys(this.obj).length === this.capacity) {
        const [k, [val, count]] = Object.entries(this.obj).reduce((acc, curr) => {
            return curr[1][1] < acc[1][1] ? curr : acc;    
        });
        delete this.obj[k];
    }
    this.obj[key] = [value, ++this.counter];
};

/** 
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */