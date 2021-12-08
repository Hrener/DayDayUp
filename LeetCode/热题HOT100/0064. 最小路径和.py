#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren
"""
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。

示例 1：
输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。

示例 2：
输入：grid = [[1,2,3],[4,5,6]]
输出：12

提示：
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 200
    0 <= grid[i][j] <= 100
    通过次数226,825提交次数330,
"""

# 动态规划
# 示例一的最终动态规划矩阵：[[1, 4, 5],
#                            [2, 7, 6],
#                            [6, 8, 7]]


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[0]*cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                # 初始化起点、边缘
                if i == 0 and j == 0:
                    dp[i][j] = grid[0][0]
                elif i == 0 and j > 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif i > 0 and j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                # 一般情况
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]     # 状态转移
        return dp[-1][-1]


# 暴力递归（超时）
"""class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0]) 
        self.cur_min = 2**100
        self.res = []
        def dfs(i, j, path_sum):
            if path_sum > self.cur_min:
                return
            # print(i, j, path_sum)
            if i >= rows or j >= cols:
                return
            path_sum += grid[i][j]
            if i == rows-1 and j == cols-1:
                self.cur_min = min(self.cur_min, path_sum)
                self.res.append(path_sum)
            dfs(i+1, j, path_sum)
            dfs(i, j+1, path_sum)
        dfs(0, 0, 0)
        return min(self.res)"""
