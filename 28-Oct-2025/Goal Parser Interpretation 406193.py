# Problem: Goal Parser Interpretation - https://leetcode.com/problems/goal-parser-interpretation/description/

class Solution:
    def interpret(self, command: str) -> str:
        n = len(command)
        i = 0
        st = ""
        while i < n:
            if command[i] == "G":
                st+="G"
                i += 1
            elif command[i:i+2] == "()":
                st += "o"
                i += 2
            elif command[i:i+2] == "(a":
                st += "al"
                i += 4
        return st
            