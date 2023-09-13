// https://leetcode.com/problems/subsets-ii

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsetsWithDup = function(nums) {
  const output = []
  nums.sort()
  ;(function backtrack(path = [], start = 0) {
    output.push(path.slice())
    for (let i = start; i < nums.length; ++i) {
      if (i > start && nums[i] === nums[i - 1]) continue
      path.push(nums[i])
      backtrack(path, i + 1)
      path.pop()
    }
  })()
  return output
};