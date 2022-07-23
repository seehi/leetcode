"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
"""
from typing import List
from collections import defaultdict

class Solution:
    def intersection_of_two_arrays1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def _get_map(nums: List[int]):
            result = defaultdict(int)
            for num in nums:
                result[num] += 1
            return result
        
        nums1_map = _get_map(nums1)
        result = []
        for num in nums2:
            if nums1_map.get(num):
                result.append(num)
                nums1_map[num] -= 1
        
        return result

    def intersection_of_two_arrays2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ump = defaultdict(int)
        for num in nums1:
            ump[num] += 1
        
        arr = []
        for num in nums2:
            if ump.get(num):
                arr.append(num)
                ump[num] -= 1
        return arr