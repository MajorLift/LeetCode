// https://leetcode.com/problems/house-robber-ii

/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    if (nums.length <= 3) return Math.max(...nums)
    const candidates = [nums.slice(0, nums.length - 1), nums.slice(1)]
    const memo = Array.from({ length: 2 }, () => new Array(nums.length - 1).fill(0))
    function dp(c, i) {
        if (i < 0) return 0
        if (memo[c][i] > 0) return memo[c][i]
        return memo[c][i] = Math.max(candidates[c][i] + dp(c, i - 2), dp(c, i - 1))
    }
    return Math.max(dp(0, nums.length - 2), dp(1, nums.length - 2))
};