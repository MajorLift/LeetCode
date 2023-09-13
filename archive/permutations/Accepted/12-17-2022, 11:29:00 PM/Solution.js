// https://leetcode.com/problems/permutations

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
  const output = []
  ;(function backtrack(path = [], used = new Array(nums.length).fill(false)) {
    if (path.length === nums.length) {
      output.push(path.slice())
      return
    }
    for (let i = 0; i < nums.length; ++i) {
      if (!used[i]) {
        used[i] = true
        path.push(nums[i])
        backtrack(path, used)
        path.pop()
        used[i] = false
      }
    }
  })()
  return output
};