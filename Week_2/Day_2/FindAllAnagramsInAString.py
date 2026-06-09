# Anagrams in a string
from collections import Counter

class Solution:
    def findAnagrams(self, s, p):

        k = len(p)
        ans = []

        if k > len(s):
            return ans

        p_count = Counter(p)
        s_count = Counter(s[:k])

        if p_count == s_count:
            ans.append(0)

        for i in range(k, len(s)):
            s_count[s[i]] += 1
            s_count[s[i-k]] -= 1

            if s_count[s[i-k]] == 0:
                del s_count[s[i-k]]

            if s_count == p_count:
                ans.append(i - k + 1)

        return ans      