#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述：

请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""

"""
示例1
输入："We Are Happy"
返回值："We%20Are%20Happy"
"""


class Solution:
    def replaceSpace(self , s ):
        # write code here
        res = ""
        for ss in s:
            res += "%20" if ss == " " else ss
        return res
