from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        lastzero = 0
        for curr in range(len(nums)):
            if nums[curr] != 0:
                nums[lastzero], nums[curr] = nums[curr], nums[lastzero]
                lastzero += 1


s = Solution()
arr = [2, 1, 0, 3, 0, 12]
s.moveZeroes(arr)
print(arr)
