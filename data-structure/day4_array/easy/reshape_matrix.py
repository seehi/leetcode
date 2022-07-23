"""
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]

Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]
"""

from typing import List

class Solution:
    def matrixReshape1(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        """思路一：
        1. 把二维数组变成一维
        2. 根据行数进行分割
        """
        mylist = []
        for i in mat:
            for j in i:
                mylist.append(j)
        
        result = []
        col_count = len(mylist)//r
        if col_count != c:
            return mat
        for i in range(r):
            start = col_count*i
            result.append(mylist[start:(col_count+start)])
        return result

    
    def matrixReshape2(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        """思路二：
        使用列表推导和range进行代码优化
        """
        if len(mat) * len(mat[0]) != r * c:
            return mat
        
        mylist = [j for i in mat for j in i]
        return [mylist[i:i+c] for i in range(0, len(mylist), c)]