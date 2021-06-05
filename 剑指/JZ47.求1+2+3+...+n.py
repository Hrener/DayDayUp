#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
示例1
输入：5
返回值：15
"""

"""
思路：
    递归
    结束递归条件：return 1 and 0
"""


class Solution:
    def Sum_Solution(self, n):
        # write code here
        return n and n + self.Sum_Solution(n-1)
