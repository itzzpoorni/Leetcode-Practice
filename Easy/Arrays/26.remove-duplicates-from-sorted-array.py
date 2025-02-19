#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        arr={}
        arr1=[]
        for i in nums:
            if i not in arr:
                arr[i]=1
            else:
                arr[i]+=1
        nums[:] = list(arr.keys())
        
# @lc code=end

