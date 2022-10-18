# https://leetcode.com/problems/missing-number/

from tkinter import N
from typing import List


class Solution1:
    def missingNumber(self, nums: List[int]) -> int:
        s = (len(nums) + 1) * len(nums) // 2

        for n in nums:
            s -= n

        return s


class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i, n in enumerate(nums):
            res += i - n

        return res
