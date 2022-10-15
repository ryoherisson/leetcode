# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        cur = 1
        prev = 0

        for _ in range(n):
            temp = cur
            cur = cur + prev
            prev = temp

        return cur
