// https://leetcode.com/problems/first-unique-character-in-a-string

/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
    const map = s.split('').reduce((acc, curr, i) => {
        if (acc.has(curr)) {
            const [count, idx] = acc.get(curr);
            acc.set(curr, [count + 1, i]);
        }
        else acc.set(curr, [1, i]);
        return acc;
    }, new Map());
    for (const [key, value] of map) {
        if (value[0] === 1) return value[1];
    }
    return -1;
};