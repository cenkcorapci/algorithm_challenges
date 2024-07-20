from typing import List


class Solution:
    def findPivotPoint(self, nums: List[int], start: int, end: int) -> int:
        pivot_right = nums[0]
        pivot_left = nums[-1]
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < pivot_right:
                pivot_right = nums[mid]
                end = mid - 1
            else:
                start = mid + 1

    def binarySearch(self, nums: List[int], target: int, start: int, end: int) -> int:
        if start > end:
            return -1
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        if nums[start] <= nums[mid]:
            if nums[start] <= target <= nums[mid]:
                return self.binarySearch(nums, target, start, mid - 1)
            return self.binarySearch(nums, target, mid + 1, end)
        if nums[mid] <= target <= nums[end]:
            return self.binarySearch(nums, target, mid + 1, end)
        return self.binarySearch(nums, target, start, mid - 1)

    def search(self, nums: List[int], target: int) -> int:
        # 4,5,6,7,0,1,2
        if not nums:
            return -1
        return self.binarySearch(nums, target, 0, len(nums) - 1)
