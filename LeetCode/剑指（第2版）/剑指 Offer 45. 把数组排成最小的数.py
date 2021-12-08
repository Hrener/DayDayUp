#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren
"""
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

示例 1:
输入: [10,2]
输出: "102"
示例 2:
输入: [3,30,34,5,9]
输出: "3033459"

提示:
0 < nums.length <= 100
"""


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        nums = [str(i) for i in nums]
        for i in range(len(nums)-1):
            for j in range(len(nums)-i-1):
                if nums[j] + nums[j+1] > nums[j+1] + nums[j]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return "".join(nums)
