# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_swap = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[last_swap]=nums[last_swap],nums[i]
                last_swap+=1