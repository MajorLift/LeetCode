// https://leetcode.com/problems/generate-parentheses

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def backtrack(tmp = "(", numOpen = 1, numClose = 0):
            if numOpen == numClose == n:
                output.append(tmp)
                return
            if numOpen < n:
                backtrack(tmp + "(", numOpen + 1, numClose)
            if numClose < numOpen <= n:
                backtrack(tmp + ")", numOpen, numClose + 1)
        backtrack()
        return output