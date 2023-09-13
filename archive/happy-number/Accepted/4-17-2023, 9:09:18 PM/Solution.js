// https://leetcode.com/problems/happy-number

/**
 * @param {number} n
 * @return {boolean}
 */
function isHappy(n) {
    let [slow, fast] = [sumOfSquares(n), sumOfSquares(sumOfSquares(n))]
    while (true) {
        if (fast === 1) return true
        if (slow === fast) return false
        ;[slow, fast] = [sumOfSquares(slow), sumOfSquares(sumOfSquares(fast))]
    }
}
function sumOfSquares(n) {
    const [last, rest] = [n % 10, Math.floor(n / 10)]
    return last ** 2 + (n === 0 ? 0 : sumOfSquares(rest))
}