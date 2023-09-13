// https://leetcode.com/problems/happy-number

/**
 * @param {number} n
 * @return {boolean}
 */
function isHappy(n) {
    let [slow, fast] = [n, sumOfSquares(n)]
    while (true) {
        if (fast === 1) return true
        if (slow === fast) return false
        ;[slow, fast] = [sumOfSquares(slow), sumOfSquares(sumOfSquares(fast))]
    }
}
function sumOfSquares(n) {
    return n === 0 
        ? 0 
        : (n % 10) ** 2 + sumOfSquares(Math.floor(n / 10))
}