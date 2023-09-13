// https://leetcode.com/problems/range-addition

/**
 * @param {number} length
 * @param {number[][]} updates
 * @return {number[]}
 */
var getModifiedArray = function(length, updates) {
    const output = new Array(length).fill(0);
    for (const [start, end, inc] of updates)
        for (let i = start; i <= end; i += 1) output[i] += inc;
    return output;
};