# https://leetcode.com/problems/group-anagrams/

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping the charCount to List of Anagrams

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(s)

        return res.values()
