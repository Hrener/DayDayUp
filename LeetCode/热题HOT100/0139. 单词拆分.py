#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
说明：
拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。

示例 1：
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。

示例 2：
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。

示例 3：
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
"""

# 暴力递归（超时）
"""class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.res = False
        def dfs(new_s):
            if len(new_s) > len(s):
                return
            if new_s == s:
                self.res = True
            if new_s != s[:len(new_s)]:
                return
            for i in range(len(wordDict)):
                dfs(new_s+wordDict[i])
        dfs("")
        return self.res"""

"""
动态规划：
    假设 s = s1 + s2 + s3
    dp[s3] = (s3 = word) 且 dp[s2] = True
    为了保留当前word使dp = True的状态，避免在后续其它word使dp = False时将其覆盖，加上或运算
    dp[s3] |= (s3 = word) 且 dp[s2] = True
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)      # 初始化，当s为""时为True
        for i in range(1, len(s) + 1):
            for word in wordDict:
                n = len(word)
                if n <= i:
                    dp[i] |= (s[i - n:i] == word) and dp[i - n]
        return dp[-1]
