// https://leetcode.com/problems/combination-sum

/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(nums, target) {
  const output = []
  ;(function backtrack(path = [], start = 0, remainder = target) {
    if (remainder === 0) output.push(path.slice())
    for (let i = start; i < nums.length; ++i) {
      if (remainder - nums[i] >= 0) {
        path.push(nums[i])
        backtrack(path, i, remainder - nums[i])
        path.pop()
      }
    }
  })()
  return output
};