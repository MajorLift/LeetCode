// https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero

/**
 * @param {number} n
 * @return {number[]}
 */
var sumZero = function(n) {
    const output = n % 2 === 0 ? [] : [0];
    for (let i = 1; i < Math.ceil(n / 2); i++) {
        output.push(-i, i);
    }
    return output;
};