// https://leetcode.com/problems/happy-number

/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    let slow = fast = n
    do {
        slow = sumOfSquares(slow)
        fast = sumOfSquares(sumOfSquares(fast))
    } while (slow !== fast)
    if (fast === 1) return true
    return false
}

function sumOfSquares(n) {
    let [last, rest] = [n % 10, Math.floor(n / 10)]
    if (rest === 0) return last ** 2 
    return last ** 2 + sumOfSquares(rest)
}