#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

给定一个数组，找出其中最小的K个数。例如数组元素是4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。如果K>数组的长度，那么返回一个空的数组

示例1
输入：[4,5,1,6,2,7,3,8],4
返回值：[1,2,3,4]
"""

"""
排序后 切片
"""

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput):return []
#         tinput.sort()

        def split(array, l, r):
            mid = array[l]
            while l < r:
                while l < r and array[r] >= mid:
                    r -= 1
                array[l] = array[r]
                while l < r and array[l] <= mid:
                    l += 1
                array[r] = array[l]
            array[l] = mid
            return l

        def quicksort(array, left, right):
            if left >= right:
                return
            mid = split(array, left, right)
            quicksort(array, left, mid-1)
            quicksort(array, mid+1, right)
        quicksort(tinput, 0, len(tinput)-1)
        return tinput[:k]
