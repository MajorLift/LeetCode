// https://leetcode.com/problems/permutations-ii

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permuteUnique = function(nums) {
  const output = []
  ;(function backtrack(start = 0) {
    if (start === nums.length) output.push(nums.slice())
    const used = new Set()
    for (let i = start; i < nums.length; ++i) {
      if (!used.has(nums[i])) {
        [nums[start], nums[i]] = [nums[i], nums[start]]
        backtrack(start + 1)
        ;[nums[start], nums[i]] = [nums[i], nums[start]]
        used.add(nums[i])
      }
    }
  })()
  return output
};