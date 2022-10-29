# https://leetcode.com/problems/container-with-most-water/

from typing import List


# Brute force
class Solution1:
    def maxArea(self, height: List[int]) -> int:
        res = 0

        for l in range(len(height)):
            for r in range(l + 1, len(height)):
                area = (r - l) * min(height[l], height[r])
                res = max(res, area)

        return res


class Solution2:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                r -= 1

        return res

