# https://leetcode.com/problems/plus-one/
from typing import List


class Solution1:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)
        res = []
        temp = 1

        for i in range(l):
            temp = temp + digits[l - i - 1]

            res.append(temp % 10)

            if temp > 9:
                temp = 1
            else:
                temp = 0

        if temp == 1:
            res.append(1)

        return res[::-1]


class Solution2:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        one, i = 1, 0

        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            else:
                digits.append(1)
                one = 0
            i += 1

        return digits
