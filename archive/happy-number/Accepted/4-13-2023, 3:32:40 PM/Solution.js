// https://leetcode.com/problems/happy-number

/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    const hashset = new Set()
    let curr = n
    while (true) {
        curr = sumOfSquares(curr)
        if (hashset.has(curr)) return false
        if (curr === 1) return true
        hashset.add(curr)
    }
};

function sumOfSquares(n) {
    let [last, rest] = [n % 10, Math.floor(n / 10)]
    if (rest === 0) return last ** 2 
    return last ** 2 + sumOfSquares(rest)
}