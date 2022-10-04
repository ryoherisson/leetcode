# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         res = 0

#         current_price = prices[0]

#         for i, p in enumerate(prices):
#             if i > 0:
#                 if p - current_price > res:
#                     res = p - current_price
#                 elif p < current_price:
#                     current_price = p

#         return res



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_p = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_p = max(max_p, profit)
            else:
                l = r
            r += 1

        return max_p
