#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

统计一个数字在升序数组中出现的次数。

示例1
输入：[1,2,3,3,3,3,4,5],3
返回值：4
"""


class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        return data.count(k)
