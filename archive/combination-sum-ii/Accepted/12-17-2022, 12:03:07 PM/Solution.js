// https://leetcode.com/problems/combination-sum-ii

/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum2 = function(nums, target) {
  const output = []
  nums.sort()
  ;(function backtrack(path = [], start = 0, remainder = target) {
    if (remainder === 0) output.push(path.slice())
    for (let i = start; i < nums.length; ++i) {
      if (i > start && nums[i] === nums[i - 1]) continue
      if (remainder - nums[i] >= 0) {
        path.push(nums[i])
        backtrack(path, i + 1, remainder - nums[i])
        path.pop()
      }
    }
  })()
  return output
};