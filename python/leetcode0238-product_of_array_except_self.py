#

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        for i in range(1, len(nums)):
            res[0] *= nums[i]


        for i in range(1, len(nums)):
            res.append(res[i-1] // nums[i] * nums[i-1])


        return res
