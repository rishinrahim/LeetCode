# Title: 'Conmtains duplicate (3/75 leetcode)'
# Author: Rishin Rahim <rishin07@gmail.com>
# Created: 2021-04-08
# Copyright (C) 2021 Rishin Rahim

"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up:

Could you solve it in O(n) time complexity and without using division?
Could you solve it with O(1) constant space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

class Solution:
    def productExceptSelf(self, nums: list) -> list:
        p = []
        nz = 0
        prod = 1
        for num in nums:
            if num == 0:
                nz = nz+1
            else:
                prod = prod*num
        if nz > 1:
            return [0]*len(nums)
        elif nz == 1:
            return [0 if i!=0 else prod for i in nums]
        else:
            return [prod//i for i in nums]

if __name__=="__main__" :
    n1 = [1,2,3,4]
    n2 = [-1,1,0,-3,3]
    s = Solution()
    print(s.productExceptSelf(n1))
    print(s.productExceptSelf(n2))
    
       
"""
Solution :
Runtime: 220 ms, faster than 98.28% of Python3 online submissions for Product of Array Except Self.
Memory Usage: 21.3 MB, less than 51.36% of Python3 online submissions for Product of Array Except Self.   
"""