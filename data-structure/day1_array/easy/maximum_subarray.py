"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

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

1 <= nums.length <= 105
-104 <= nums[i] <= 104
"""
from typing import List
class Solution:
    """思路一: 暴力破解, 一个数相加、两个数相加...
    """
    def maxSubArray1(self, nums: List[int]) -> int:
        nums_len = len(nums)
        if nums_len == 1:
            return nums[0]
        max = nums[0]
        for i in range(nums_len):
            print(f"add length: {i}, total: {nums_len}")
            j = 0
            while j < nums_len - i:
                count = sum(nums[j:j+i+1])
                if count > max:
                    max = count
                j += 1
        return max

    """思路二: 找到未检查过的第一个正数, 叠加后面的数, 直到和小于零或是到末尾
    """
    def maxSubArray2(self, nums: List[int]) -> int:
        nums_len = len(nums)
        if nums_len == 1:
            return nums[0]
        max, start = nums[0], 0
        while start < nums_len:
            if nums[start] < 0:
                if nums[start] > max:
                    max = nums[start]
                start += 1
                continue
            if nums[start] > max:
                max = nums[start]
            if start == nums_len - 1:
                break
            sum_from_start = nums[start]  
            for i in range(start+1, nums_len):
                sum_from_start += nums[i]
                if sum_from_start > max:
                    max = sum_from_start
                if sum_from_start < 0:
                    start = i + 1
                    break
                if i == nums_len - 1:
                    start = nums_len
                    break
        return max
    
    """思路三: 循环一遍, 叠加每个数字, 若当前和不小于零, 则继续, 否则当前和设置为零, 相当于新的开始
    """
    def maxSubArray3(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = 0
        for num in nums:
            current_sum += num
            max_sum = max(max_sum, current_sum)
            if current_sum < 0:
                current_sum = 0
        return max_sum
            
    """思路四：什么时候开始新起炉灶，把当前值和（之前和+当前值）相比，如果当前值较大，则可以新起炉灶
    """
    def maxSubArray4(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_sum, cur_sum = nums[0], nums[0]
        for i in range(1, len(nums)):
            cur_sum = max(nums[i], cur_sum+nums[i])
            max_sum = max(max_sum, cur_sum)
        return max_sum