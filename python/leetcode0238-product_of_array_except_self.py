#

from typing import List


class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        zero_count = 0
        product = 1

        for i in range(0, len(nums)):
            if nums[i] == 0:
                zero_count += 1
                continue

            product *= nums[i]

        if zero_count > 1:
            return [0] * len(nums)

        for i in range(0, len(nums)):
            if zero_count == 1:
                if nums[i] == 0:
                    res[i] = product
                else:
                    res[i] = 0
            else:
                res[i] = product // nums[i]

        return res

class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
