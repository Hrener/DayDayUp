#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
返回值描述：对应每个测试案例，输出两个数，小的先输出。
            如果没有返回[]

示例1
输入：[1,2,4,7,11,15],15
返回值：[4,11]
"""

"""
思路：
    双指针
"""


class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        self.res = []
        left = 0
        while left < len(array)-1:
            right = left + 1
            while right < len(array) and array[right] <= tsum:
                if array[left] + array[right] == tsum:
                    if not self.res:
                        self.res = [array[left], array[right]]
                    else:
                        if array[left] * array[right] < self.res[0] * self.res[1]:
                            self.res = [array[left], array[right]]
                right += 1
            left += 1
        return self.res
