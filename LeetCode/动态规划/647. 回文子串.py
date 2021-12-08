#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren
"""
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

示例 1：
输入："abc"
输出：3
解释：三个回文子串: "a", "b", "c"

示例 2：
输入："aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
 
提示：输入的字符串长度不会超过 1000 。
"""

"""
递归：
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        def dfs(tem, s_li):
            if len(tem)>0 and tem == tem[::-1]:
                self.res += 1
            if not s_li:return
            if not tem:
                for i in range(len(s)):
                    dfs(tem+s[i], s[i+1:])
            else:
                dfs(tem+s_li[0], s_li[1:])
        self.res = 0
        dfs("", s)
        return self.res

"""
动态规划，上三角dp数组，对角线方向遍历，当前状态 = 第i位是否等于第j位 and dp[i+1][j-1]
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[1]*(i+1)+[0]*(len(s)-i-1) for i in range(len(s))]
        self.res = len(s)
        for i in range(1, len(s)):
            for j in range(len(s)-i):
                if s[j] == s[j+i] and dp[j+1][j+i-1]:
                    dp[j][j+i] = 1
                    self.res += 1
        return self.res
