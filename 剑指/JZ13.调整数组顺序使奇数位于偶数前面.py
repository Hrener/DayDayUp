#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

示例1
输入：[1,2,3,4]
返回值：[1,3,2,4]
示例2
输入：[2,4,6,5,7]
返回值：[5,7,2,4,6]
"""

"""
此代码不开辟新的数组，但会超时
"""


class Solution:
    def reOrderArray(self , array ):
        # write code here
        left = 0
        right = 0
        while right < len(array):
            while left < len(array)  and array[left] % 2 == 1:
                left += 1
            right = left
            while right < len(array) and array[right] % 2 == 0:
                right += 1
            if right == len(array): return array
            tem = array[right]
            array[left+1:right+1] = array[left:right]
            array[left] = tem
#             print(left, right, array)
            left = left + 1
        return array


