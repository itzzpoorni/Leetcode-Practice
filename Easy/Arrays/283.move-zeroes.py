#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """    
        Do not return anything, modify nums in-place instead.
        """
        s=len(nums)
        res=[0]*(s)
        j=0
        for i in range(s):
            if nums[i]!=0:
                res[j]=nums[i]
                j=j+1
        nums[:]=res
        
# @lc code=end

