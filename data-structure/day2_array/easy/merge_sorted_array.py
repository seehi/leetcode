from typing import List


class Solution:
    """思路一：双指针"""
    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums3 = nums1[:m]
        nums4 = nums2[:n]
        i, j, i_max, j_max = 0, 0, len(nums3)-1, len(nums4)-1
        k = 0
        while i <= i_max and j <= j_max:
            if nums3[i] <= nums4[j]:
                nums1[k] = nums3[i]
                i += 1
            else:
                nums1[k] = nums4[j]
                j += 1
            k += 1

        nums1[k:] = nums4[j:] if i > i_max else nums3[i:]


    """思路二：把nums2的内容放到nums1，然后使用内置sort排序"""
    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:n]
        nums1.sort()


if __name__ == "__main__":
    s = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    s.merge(nums1, 3, nums2, 3)
    print(nums1)
            
        