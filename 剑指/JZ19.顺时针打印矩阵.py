#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵：
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

示例1
输入：[[1,2],[3,4]]
返回值：[1,2,4,3]
"""


class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
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
