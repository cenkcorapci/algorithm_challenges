class Solution:
    def rotate(self, nums, k):
        k = k % len(nums)
        n = len(nums)
        i = 0
        count = 0
        while count < n:
            pos = (i + k) % len(nums)
            curr = nums[pos]
            nums[pos] = nums[i]
            count += 1
            j = pos
            while j != i and count < n:
                pos = (j + k) % len(nums)
                nums[pos], curr = curr, nums[pos]
                j = pos
                count += 1
            i += 1


s = Solution()

arr = [-1, 3, 1, 99]
s.rotate(arr, 2)
print(arr)

arr = [1, 2, 3, 4, 5, 6, 7]
s.rotate(arr, 3)
print(arr)
