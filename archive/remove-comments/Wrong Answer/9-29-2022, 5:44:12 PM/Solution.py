// https://leetcode.com/problems/remove-comments

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        block_sw = False
        output = []
        for line in source:
            parsed = ""
            if block_sw:
                parsed = output.pop()
            i = 0
            while i < len(line):
                if i < len(line) - 1 and line[i] == line[i + 1] == "/":
                    break
                if i < len(line) - 1 and line[i] == "/" and line[i + 1] == "*":
                    block_sw = True
                    i += 2
                if block_sw:
                    if i < len(line) - 1 and line[i] == "*" and line[i + 1] == "/":
                        block_sw = False
                        i += 2
                    else:
                        i += 1
                else:
                    parsed += line[i]
                    i += 1
            if len(parsed):
                output.append(parsed)
        return output