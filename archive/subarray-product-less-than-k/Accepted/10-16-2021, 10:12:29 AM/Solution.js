// https://leetcode.com/problems/subarray-product-less-than-k

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var numSubarrayProductLessThanK = function(nums, k) {
    let [product, counter] = [1, 0];
    let [left, right] = [0, 0];
    while (true) {
        product *= nums[right];
        if (product < k) {
            counter++;
            if (right < nums.length - 1) right++;
            else {
                product = 1;
                right = ++left;
            }
        }
        else {
            product = 1;
            if (left < nums.length - 1) right = ++left;
            else break;
        }
    }
    return counter;
};