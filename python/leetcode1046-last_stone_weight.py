# https://leetcode.com/problems/last-stone-weight/

import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.heapq = stones

        self.heapq = list(map(lambda x: -x, self.heapq))

        heapq.heapify(self.heapq)

        while len(self.heapq) > 1:
            y = heapq.heappop(self.heapq)
            x = heapq.heappop(self.heapq)

            if -x < -y:
                new_y = y - x
                heapq.heappush(self.heapq, new_y)

        self.heapq.append(0)
        return abs(self.heapq[0])
