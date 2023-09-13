/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var smallestRangeI = function(nums, k) {
    return Math.max(0, Math.max(...nums) - Math.min(...nums) - 2 * k)
};
