# String Compression
class Solution:
    def compress(self, chars):
        i = 0
        ans = []

        while i < len(chars):
            ch = chars[i]
            count = 0

            while i < len(chars) and chars[i] == ch:
                count += 1
                i += 1
            ans.append(ch)

            if count > 1:
                ans.extend(list(str(count)))

        chars[:] = ans
        return len(chars)       