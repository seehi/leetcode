"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""
from typing import List
from collections import defaultdict

class Solution:
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        """ 思路一：
            新建一个字典，键为num，值为num下标
        """
        m = defaultdict(list)
        for i, num in enumerate(nums):
            m[num].append(i)
            
            gap = target - num
            if gap in m and m[gap][0] != i:
                return m[gap][0], i
    
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        """ 思路二：
            新建一个字典，键为target-num，值为num下标
        """
        m = {}
        for i, num in enumerate(nums):
            if num in m:
                return m[num], i
            
            m[target-num] = i
    
    """Given any array of integers nums and an integer target, return indices of the two numbers such that they add up to target."""
    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        """ 思路三：
            先排序，再遍历
        """
        nums.sort()
        left, right = 0, len(nums)-1
        while left < right:
            sum = nums[left] + nums[right]
            if sum == target:
                return left, right
            elif sum < target:
                left += 1
            else:
                right -= 1
        return -1, -1


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum3([3,2,4], 6))