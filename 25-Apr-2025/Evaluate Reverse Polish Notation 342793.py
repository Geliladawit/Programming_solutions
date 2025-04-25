# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        dig = []
        for i in tokens:
            if i == "/":
                x = int(dig[-2]) / int(dig[-1])
                dig.pop()
                dig.pop()
                dig.append(x)
            elif i == "*":
                x = int(dig[-2])* int(dig[-1])
                dig.pop()
                dig.pop()
                dig.append(x)
            elif i == "+":
                x = int(dig[-2])+ int(dig[-1])
                dig.pop()
                dig.pop()
                dig.append(x)
            elif i == "-":
                x = int(dig[-2]) - int(dig[-1])
                dig.pop()
                dig.pop()
                dig.append(x)
            else:
                dig.append(int(i))
        return int(dig[0])
