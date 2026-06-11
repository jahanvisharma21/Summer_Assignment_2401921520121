# Decode String
class Solution:
    def decodeString(self, s):
        stack = []
        num = 0
        res = ""
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == '[':
                stack.append((res, num))
                res = ""
                num = 0

            elif ch == ']':
                prev, n = stack.pop()
                res = prev + res * n

            else:
                res += ch

        return res        