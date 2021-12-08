#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren
"""
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1：
输入：[3,2,3]
输出：3

示例 2：
输入：[2,2,1,1,1,2,2]
输出：2
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict_ = {}
        base = len(nums)//2
        for num in nums:
            if num not in dict_:
                dict_[num] = 0
            dict_[num] += 1
            if dict_[num] > base:
                return num
