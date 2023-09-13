// https://leetcode.com/problems/divide-two-integers

/**
 * @param {number} dividend
 * @param {number} divisor
 * @return {number}
 */
var divide = function(dividend, divisor) {
    let quotient = 0;
    while (dividend >= divisor) {
        dividend -= divisor;
        quotient += 1;
    }
    return quotient > Math.pow(2, 31) - 1 ? Math.pow(2, 31) - 1 : quotient < -1 * Math.pow(2, 31) ? -1 * Math.pow(2, 31) : quotient;
};