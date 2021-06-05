#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

示例1
输入：[3,4,5,1,2]
返回值：1
"""

"""
思路：二分
mid = left + (right - left)//2
    1. 当left值大于mid值时，最小值一定在前半段，因此right = mid
    2. 当left值小于mid值时，最小值一定在后半段，因此left = mid

应注意的是：取mid值时向下取整，导致最后剩下两个数时，最小值一定在right处
"""


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0: return 0
        left = 0
        right = len(rotateArray) - 1
        while right - left > 1:
            mid = left + (right - left)//2
            if rotateArray[left] > rotateArray[mid]:
                right = mid
            else:
                left = mid
        return rotateArray[right]
