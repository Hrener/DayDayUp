#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren
"""
统计一个数字在排序数组中出现的次数。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2

示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = 0
        for num in nums:
            if num == target:res += 1
        return res
