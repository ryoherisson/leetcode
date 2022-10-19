# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set() # Memory O(n)

        while n not in visit:
            visit.add(n)
            n = self.sum_of_square(n)

            if n == 1:
                return True

        return False

    def sum_of_square(self, n: int) -> int:
        output = 0

        while n:
            output += (n % 10)**2
            n //= 10

        return output
