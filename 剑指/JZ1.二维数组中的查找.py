#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren


"""
描述：

在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
[[1,2,8,9],
  [2,4,9,12],
  [4,7,10,13],
  [6,8,11,15]]

给定 target = 7，返回 true。
给定 target = 3，返回 false。

示例1
输入：7,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
返回值：true 说明：存在7，返回true
示例2
输入：3,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
返回值：false 说明：不存在3，返回false
"""

"""
思路是：
利用二维数组由上到下，由左到右递增的规律，
选取左上角的元素a[row][col]与target进行比较，
当target小于元素a[row][col]时，那么target必定在元素a所在行的左边,即col--；
当target大于元素a[row][col]时，那么target必定在元素a所在列的下边,即row++；
"""


class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        row = 0
        col = len(array[0])-1
        while row < len(array) and col > -1:
            if target < array[row][col]:
                col -= 1
            elif target > array[row][col]:
                row += 1
            else:
                return True
        return False




