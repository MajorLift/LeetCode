// https://leetcode.com/problems/spiral-matrix

/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
   let [nr, nc] = [matrix.length, matrix[0].length]
   const output = []
   while (nr >= 1 || nc >= 1) {
      output.push(...(matrix.shift() ?? []))
      nr--

      if (!matrix[0]?.length) break
      for (let i = 0; i < nr; ++i) {
         output.push(matrix[i].pop())
      }
      nc--

      output.push(...(matrix.pop()?.reverse() ?? []))
      nr--

      if (!matrix[0]?.length) break
      for (let i = nr - 1; i >= 0; --i) {
         output.push(matrix[i].shift())
      }
      nc--
   }
   if (matrix[0]?.length) output.push(...matrix[0])
   return output
};