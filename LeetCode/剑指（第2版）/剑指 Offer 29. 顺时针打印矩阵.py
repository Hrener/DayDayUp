#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren
"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

示例 2：
输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]

限制：
0 <= matrix.length <= 100
0 <= matrix[i].length <= 100
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # write code here
        if not matrix:return []
        xmin = 0
        xmax = len(matrix)
        ymin = 0
        ymax = len(matrix[0])
        res = []

        matric_N = xmax * ymax
        while True:
            [res.append(matrix[xmin][col]) for col in range(ymin, ymax)]
            xmin += 1
            if len(res) == matric_N: break
            [res.append(matrix[row][ymax - 1]) for row in range(xmin, xmax)]
            ymax -= 1
            if len(res) == matric_N: break
            [res.append(matrix[xmax - 1][col]) for col in range(ymax - 1, ymin - 1, -1)]
            xmax -= 1
            if len(res) == matric_N: break
            [res.append(matrix[row][ymin]) for row in range(xmax - 1, xmin - 1, -1)]
            ymin += 1
            if len(res) == matric_N: break
        return res
