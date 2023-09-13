// https://leetcode.com/problems/n-queens

/**
 * @param {number} n
 * @return {string[][]}
 */
var solveNQueens = function(n) {
    const output = []
    const board = Array.from({ length: n }, () => new Array(n).fill(true))
    ;(function backtrack(row = 0, state = board) {
        if (row === n) {
            output.push(state.map((row) => row.map((e) => (e !== "Q" ? "." : "Q")).join('')))
            return
        }
        for (let col = 0; col < n; ++col) {
            if (!state[row][col]) continue
            const newState = JSON.parse(JSON.stringify(state))
            for (let i = 0; i < n; ++i) {
                newState[row][i] = false
                newState[i][col] = false
                if (row + i < n) {
                    if (col + i < n) newState[row + i][col + i] = false
                    if (col - i >= 0) newState[row + i][col - i] = false
                }
            }
            newState[row][col] = "Q"
            backtrack(row + 1, newState)
        }
    })()
    return output    
}