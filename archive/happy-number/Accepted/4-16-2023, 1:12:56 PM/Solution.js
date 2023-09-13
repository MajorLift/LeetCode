// https://leetcode.com/problems/happy-number

/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    let [slow, fast] = [sumOfSquares(n), sumOfSquares(sumOfSquares(n))]
    while (true) {
        if (fast === 1) return true
        if (slow === fast) return false
        slow = sumOfSquares(slow)
        fast = sumOfSquares(sumOfSquares(fast))
    }
}

function sumOfSquares(n) {
    return (n % 10) ** 2 + (n === 0 ? 0 : sumOfSquares(Math.floor(n / 10)))
}