// https://leetcode.com/problems/subsets

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
  const output = []
  ;(function backtrack(path, start) {
    output.push(path.slice())
    for (let i = start; i < nums.length; ++i) {
      path.push(nums[i])
      backtrack(path, i + 1)
      path.pop()
    }
  })([], 0)
  return output
};