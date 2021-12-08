#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren
"""
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例:
s = "abaccdeff"
返回 "b"

s = ""
返回 " "
限制：
0 <= s 的长度 <= 50000
"""

# class Solution:
#     def firstUniqChar(self, s: str) -> str:
#         if not s:return " "
#         for i in range(len(s)):
#             if s[i] not in s[:i]+s[i+1:]:
#                 return s[i]
#         return " "

class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        if not s: return ' '
        for word in s:
            if word not in dic:dic[word] = 0
            dic[word] += 1
        for k,v in dic.items():
            if v == 1: return k
        return ' '
