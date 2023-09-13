// https://leetcode.com/problems/sign-of-the-product-of-an-array

/**
 * @param {number[]} nums
 * @return {number}
 */
var arraySign = function(nums) {
    return nums.reduce((acc, curr) => (curr > 0 ? acc : curr < 0 ? -1 * acc : 0), +1)
};