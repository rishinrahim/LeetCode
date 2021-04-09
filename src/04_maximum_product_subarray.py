"""
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""

class Solution:
    
    def maxProduct(self, nums: list) -> int:
        max_curr = min_curr = max_global = nums[0]
        print(nums)
        for i in range(1,len(nums)):
            tmp = max_curr
            max_curr = max(nums[i],max_curr*nums[i],min_curr*nums[i])
            min_curr = min(nums[i],tmp*nums[i],min_curr*nums[i])
            max_global = max(max_curr,max_global)

        return max_global        
            
        
        
            
if __name__ == '__main__':
    a = [-3,-1,-1]
    b = [2,3,0,-2,4]
    c = [-2,3,-4]
    s = Solution()
    print(s.maxProduct(a))
    print(s.maxProduct(b))
    print(s.maxProduct(c))
    
