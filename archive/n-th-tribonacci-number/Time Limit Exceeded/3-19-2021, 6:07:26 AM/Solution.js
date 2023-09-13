// https://leetcode.com/problems/n-th-tribonacci-number

/**
 * @param {number} n
 * @return {number}
 */
const tribonacci = function(n) {
    switch (n) {
        case 0: return 0;
        case 1: return 1;
        case 2: return 1;
        default: return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3);
    }
};