#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例 1：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true

示例 2：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
输出：true

示例 3：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
输出：false

提示：
    m == board.length
    n = board[i].length
    1 <= m, n <= 6
    1 <= word.length <= 15
    board 和 word 仅由大小写英文字母组成
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        self.res = False

        def dfs(i, j, tem, path):
            # 保存当前tem走过的路径，若重复则结束
            if (i, j) not in path:
                path = path + [(i, j)]
            else:
                return
            # 递归结束条件
            if word[:len(tem)] != tem:
                return
            else:
                if len(tem) == len(word):
                    self.res = True
                    return
            if i - 1 >= 0: dfs(i - 1, j, tem + board[i - 1][j], path)
            if j - 1 >= 0: dfs(i, j - 1, tem + board[i][j - 1], path)
            if i + 1 < rows: dfs(i + 1, j, tem + board[i + 1][j], path)
            if j + 1 < cols: dfs(i, j + 1, tem + board[i][j + 1], path)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    dfs(row, col, board[row][col], [])
        return self.res
