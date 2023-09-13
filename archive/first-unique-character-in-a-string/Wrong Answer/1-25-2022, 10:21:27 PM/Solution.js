// https://leetcode.com/problems/first-unique-character-in-a-string

/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
    const map = s.split('').reduce((acc, curr, i) => {
        try {
            const [count, idx] = acc.get(curr);
            acc.set(curr, [++count, i]);
        }
        catch { 
            acc.set(curr, [1, i]);
        }
        return acc;
    }, new Map());
    console.log(map)
    for (const [key, value] of map) {
        if (value[0] === 1) return value[1];
    }
    return -1;
};