from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        slow = 0
        fast = 0
        while fast < len(nums):
            if slow == fast:
                fast += 1
            elif nums[slow] == nums[fast]:
                fast += 1
            elif nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
        # print(nums)
        return slow + 1


s = Solution()
print(s.removeDuplicates([1, 1, 2]))
