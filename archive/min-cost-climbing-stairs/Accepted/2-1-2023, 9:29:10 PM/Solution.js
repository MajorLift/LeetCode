// https://leetcode.com/problems/min-cost-climbing-stairs

/**
 * @param {number[]} cost
 * @return {number}
 */
var minCostClimbingStairs = function (cost) { 
  return Math.min(...cost.reduce(([acc, prev], curr) => ([Math.min(acc, prev) + curr, acc]), [0, 0]))
}