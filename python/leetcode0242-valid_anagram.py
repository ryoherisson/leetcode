'''
Solution idea
1. Sort
    time: O(nlogn), space: O(1)
2. Hashmap
    time: O(s+t), space: O(s+t)
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_map_s = dict()
        for i in s:
            hash_map_s[i] = 1 + hash_map_s.get(i, 0)

        for i in t:
            if i not in hash_map_s or hash_map_s[i] == 0:
                return False
            hash_map_s[i] -= 1
        return True
