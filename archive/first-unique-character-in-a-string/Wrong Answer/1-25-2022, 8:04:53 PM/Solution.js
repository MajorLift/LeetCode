// https://leetcode.com/problems/first-unique-character-in-a-string

/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
    if (s[0] !== s[1]) return 0;
    for (let i = 1; i < s.length - 1; i++) {
        if (s[i - 1] !== s[i] && s[i] !== s[i + 1]) return i;
    }
    return -1;
};