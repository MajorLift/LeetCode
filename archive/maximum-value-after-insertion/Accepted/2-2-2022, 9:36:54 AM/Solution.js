// https://leetcode.com/problems/maximum-value-after-insertion

/**
 * @param {string} n
 * @param {number} x
 * @return {string}
 */
var maxValue = function(n, x) {
    let negFlag = false;
    for (let i = 0; i < n.length; i++) {
        if (n[i] === "-") {
            negFlag = true;
            continue;
        }
        const curr = parseInt(n[i]);
        if (((!negFlag && x > curr) || (negFlag && x < curr))) {
            return n.slice(0, i) + x + n.slice(i);
        }
    }
    return n + x;
};