// https://leetcode.com/problems/maximum-value-after-insertion

/**
 * @param {string} n
 * @param {number} x
 * @return {string}
 */
var maxValue = function(n, x) {
    let negFlag = false;
    if (n[0] === "-") negFlag = true; 
    for (let i = (!negFlag ? 0 : 1); i < n.length; i++) {
        if (((!negFlag && x > parseInt(n[i])) || (negFlag && x < parseInt(n[i])))) {
            return n.slice(0, i) + x + n.slice(i);
        }
    }
    return n + x;
};