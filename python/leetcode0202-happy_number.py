# https://leetcode.com/problems/happy-number/


class Solution1:
    def isHappy(self, n: int) -> bool:
        visit = set()  # Memory O(n)

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


class Solution2:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, n

        while fast != 1:
            slow = self.sum_of_square(slow)
            fast = self.sum_of_square(self.sum_of_square(fast))

            if slow != 1 and slow == fast:
                return False

        return True

    def sum_of_square(self, n: int) -> int:
        output = 0

        while n:
            output += (n % 10)**2
            n //= 10

        return output
