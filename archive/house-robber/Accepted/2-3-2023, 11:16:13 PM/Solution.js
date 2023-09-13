// https://leetcode.com/problems/house-robber

/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    return nums.reduce(([acc, prev], curr) => ([Math.max(curr + prev, acc), acc]), [0, 0])[0]
}