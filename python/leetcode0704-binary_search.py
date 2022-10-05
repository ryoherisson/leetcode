# https://leetcode.com/problems/binary-search/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)

        while l < r:
            mid = (r - l) // 2 + l

            if nums[mid] > target:
                r = mid
            elif nums[mid] == target:
                return mid
            else:
                l = mid + 1
        return -1
