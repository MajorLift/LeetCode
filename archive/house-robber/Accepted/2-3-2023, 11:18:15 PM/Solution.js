// https://leetcode.com/problems/house-robber

/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    let [acc, prev] = [0, 0]
    for (const num of nums) {
        [acc, prev] = [Math.max(num + prev, acc), acc]
    }
    return acc
}