from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        max_length = 0
        for num in nums:
            if num - 1 not in nums:
                length = 1
                while num + 1 in nums:
                    num += 1
                    length += 1
                max_length = max(max_length, length)
        return max_length
