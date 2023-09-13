// https://leetcode.com/problems/word-search

/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function(board, word) {
    const [m, n] = [board.length, board[0].length]
    const wordCharsCount = word.split('').reduce((acc, curr) => {
        acc[curr] = (acc[curr] || 0) + 1
        return acc
    }, {})
    const wordCharsSet = new Set(Object.keys(wordCharsCount))
    const charCoordsMap = board.reduce((acc, row, i) => {
        row.forEach((char, j) => {
            if (wordCharsSet.has(char)) acc[char] = (acc[char] || new Set()).add(JSON.stringify([i, j]))
        })
        return acc
    }, {})

    if (m * n < word.length
        || wordCharsSet.size != Object.keys(charCoordsMap).length
        || ![...wordCharsSet].every((k) => (wordCharsCount[k] <= charCoordsMap[k].size))) 
        return false

    if (charCoordsMap[word[word.length - 1]] < charCoordsMap[word[0]]) {
        word = word.reverse()
    }

    function backtrack([x, y], idx) {
        if (idx === word.length - 1) return true
        charCoordsMap[word[idx]].delete(JSON.stringify([x, y]))
        for (const [i, j] of [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]) {
            if (!charCoordsMap[word[idx + 1]].has(JSON.stringify([i, j]))) continue
            if (backtrack([i, j], idx + 1)) return true
        }
        charCoordsMap[word[idx]].add(JSON.stringify([x, y]))
        return false
    }

    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            if (board[i][j] == word[0]) {
                if (backtrack([i, j], 0)) return true
            }
        }
    }
    return false
}