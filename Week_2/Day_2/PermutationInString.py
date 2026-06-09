# Permutation in string
from collections import Counter

class Solution:
    def checkInclusion(self, s1, s2):

        k = len(s1)

        for i in range(len(s2) - k + 1):
            if Counter(s2[i:i+k]) == Counter(s1):
                return True

        return False       