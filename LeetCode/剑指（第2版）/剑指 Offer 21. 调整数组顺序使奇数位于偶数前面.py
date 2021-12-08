#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren
"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

示例：
输入：nums = [1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。
"""


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        while left < right:
            while nums[left] % 2 != 0 and left < right:
                left += 1
            while nums[right] % 2 == 0 and left < right:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums
