'''
Solution ideas
1. Bruteforce
    time: O(n^2), space: O(1)
2. Sort
    time: O(nlogn), space: O(1)
3. HashSet
    time: O(n), space: O(n)
'''
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            else:
                hashset.add(i)
        return False
