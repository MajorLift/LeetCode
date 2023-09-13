// https://leetcode.com/problems/divide-two-integers

/**
 * @param {number} dividend
 * @param {number} divisor
 * @return {number}
 */
var divide = function(dividend, divisor) {
    if (dividend === 0) return 0;
    if (divisor === 0) return dividend >= 0 ? +Infinity : -Infinity;
    
    let quotient = 0;
    let negative = false;
    if (dividend < 0 && divisor > 0) {
        dividend *= -1;
        negative = true;
    }
    else if (dividend > 0 && divisor < 0) {
        divisor *= -1;
        negative = true;
    }
    else if (dividend < 0 && divisor < 0) {
        dividend *= -1;
        divisor *= -1;
    }
    while (dividend >= divisor) {
        dividend -= divisor;
        quotient += 1;
    }
    if (negative) quotient *= -1;
    return quotient > Math.pow(2, 31) - 1 ? Math.pow(2, 31) - 1 : quotient < -1 * Math.pow(2, 31) ? -1 * Math.pow(2, 31) : quotient;
};