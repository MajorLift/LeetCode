// https://leetcode.com/problems/valid-parentheses

/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const stack = []
    s.split('').forEach((p) => {
        if (['(', '{', '['].includes(p)) stack.push(p)
        else {
            const open = stack.pop()
            if (open !== p) return false
        }
    })
    return true
};