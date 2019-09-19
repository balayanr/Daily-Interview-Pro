"""
This problem was recently asked by Apple:

Given an array with n objects colored red, white or blue,
sort them in-place so that objects of the same color are adjacent,
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color
red, white, and blue respectively.

Note: You are not suppose to use the library’s sort function for this problem.

Can you do this in a single pass?
"""

class Solution:
    def sortColors(self, nums):
        counts = [0, 0, 0]
        for num in nums:
            counts[num] += 1
        # do it "in place"
        nums[:counts[0]] = [0] * counts[0]
        nums[counts[0]:counts[0] + counts[1]] = [1] * counts[1]
        nums[counts[0] + counts[1]:] = [2] * counts[2]
        return nums

nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
print("Before Sort: ")
print(nums)
# [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]

Solution().sortColors(nums)
print("After Sort: ")
print(nums)
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]
