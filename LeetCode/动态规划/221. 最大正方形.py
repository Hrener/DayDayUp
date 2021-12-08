#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren
"""
在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。

示例 1：
输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：4

示例 2：
输入：matrix = [["0","1"],["1","0"]]
输出：1

示例 3：
输入：matrix = [["0"]]
输出：0

提示：
m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] 为 '0' 或 '1'
"""

# dp[i][j]表示以第i行第j列为右下角所能构成的最大正方形边长


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
        area = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == "0":
                    dp[row+1][col+1] = 0
                else:
                    dp[row+1][col+1] = min(dp[row+1][col], dp[row][col+1], dp[row][col])+1
                area = max(area, dp[row+1][col+1]**2)
        return area
