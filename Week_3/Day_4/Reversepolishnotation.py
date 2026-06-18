# Evaluate Reverse Polish Notation
class Solution:
    def evalRPN(self, tokens):
        stack = []

        for ch in tokens:

            if ch not in "+-*/":
                stack.append(int(ch))

            else:
                b = stack.pop()
                a = stack.pop()

                if ch == "+":
                    stack.append(a + b)
                elif ch == "-":
                    stack.append(a - b)
                elif ch == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(float(a) / b))

        return stack[-1]                  