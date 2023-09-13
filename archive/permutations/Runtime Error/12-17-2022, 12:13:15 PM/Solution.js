// https://leetcode.com/problems/permutations

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
  const output = []
  ;(function backtrack(start = 0) {
    if (start === nums.length) output.push(nums.slice())
    else {
      for (let i = start; i < nums.length; ++i) {
        [nums[start], nums[i]] = [nums[i], nums[start]]
        backtrack(start + 1)
        [nums[start], nums[i]] = [nums[i], nums[start]]
      }
    }
  })()
  return output
};