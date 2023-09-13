// https://leetcode.com/problems/word-break

/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function(s, wordDict) {
    const wordSet = new Set(wordDict)
    const memo = new Array(s.length).fill(false)
    return (function dp(start) {
        if (!!memo[start]) return memo[start]
        if (start == s.length) return memo[start] = true
        for (let end = start + 1; end < s.length + 1; ++end) {
            if (wordSet.has(s.slice(start, end)) && dp(end)) {
                return memo[end] = true
            }
        }
        return memo[start] = false
    })(0)
};