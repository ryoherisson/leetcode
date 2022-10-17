# https://leetcode.com/problems/reverse-bits/

class Solution1:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            res *= 2
            res += n % 2
            n >>= 1

        return res

class Solution2:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res |= (bit << (31 - i))
        return res
