# Title: 'Maximum subarray'
# Author: Rishin Rahim <rishin07@gmail.com>
# Created: 2021-04-08
# Copyright (C) 2021 Rishin Rahim

"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
 

Constraints:

1 <= nums.length <= 3 * 104
-105 <= nums[i] <= 105
    
"""

class Solution:
    
    def maxSubArray(self, nums: list) -> int:
        max_curr = max_global = nums[0]
        for i in range(1,len(nums)):
            max_curr = max(nums[i],max_curr+nums[i])
            if max_curr > max_global:
                max_global = max_curr
                

        return max_global        
            
        
        
            
if __name__ == '__main__':
    a = [5,4,-1,7,8]
    b = [1]
    c = [-2,1,-3,4,-1,2,1,-5,4]
    s = Solution()
    print(s.maxSubArray(a))
    print(s.maxSubArray(b))
    print(s.maxSubArray(c))
    
"""
Runtime: 56 ms, faster than 97.41% of Python3 online submissions for Maximum Subarray.
Memory Usage: 14.9 MB, less than 80.00% of Python3 online submissions for Maximum Subarray.

 """   