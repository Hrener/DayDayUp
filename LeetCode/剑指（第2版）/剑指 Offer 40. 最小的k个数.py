#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren
"""
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

示例 1：
输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]

示例 2：
输入：arr = [0,1,2,1], k = 1
输出：[0]
"""


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        def quicksort(nums, left, right):
            if left >= right:
                return
            l = left
            r = right
            base = arr[left]
            while l < r:
                while l<r and arr[r]>=base:
                    r -= 1
                arr[l] = arr[r]
                while l<r and arr[l]<=base:
                    l += 1
                arr[r] = arr[l]
            arr[l] = base
            quicksort(nums, left, l-1)
            quicksort(nums, l+1, right)
        quicksort(arr, 0, len(arr)-1)
        return arr[:k]
