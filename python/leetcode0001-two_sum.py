'''
Solution ideas
1. Brute Force
    time O(n^2), space: O(1)
2. Sort
    time O(nlogn), space: O(1)
3. Hashmap
    time O(n), space: O(n)
'''


from typing import List

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         nums_sorted = sorted(nums)
#         left = 0
#         right = len(nums_sorted) - 1

#         while left < right:
#             sum = nums_sorted[left] + nums_sorted[right]
#             if sum == target:
#                 break

#             if sum > target:
#                 right -= 1
#             else:
#                 left += 1

#         res = []
#         for i, num in enumerate(nums):
#             if num == nums_sorted[left]:
#                 res.append(i)
#             elif num == nums_sorted[right]:
#                 res.append(i)
#         return res

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev_map:
                return [prev_map[diff], i]
            prev_map[n] = i
        return
