// https://leetcode.com/problems/house-robber

/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    const memo = new Array(nums.length).fill(null)
    return (function dp(i = nums.length - 1) {
        if (i < 0) return 0
        if (memo[i] !== null) return memo[i]
        return memo[i] = Math.max(nums[i] + dp(i - 2), dp(i - 1))
    })()
};