#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

一个整型数组里除了两个数字只出现一次，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。

示例1
输入：[1,4,1,6]
返回值：[4,6]
说明：返回的结果中较小的数排在前面
"""


class Solution:
    def FindNumsAppearOnce(self , array ):
        # write code here
        self.res = []
        for i in array:
            if array.count(i) == 1:
                self.res.append(i)
        return self.res
