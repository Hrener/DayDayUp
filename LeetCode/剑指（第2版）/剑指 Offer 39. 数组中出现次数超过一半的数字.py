#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren
"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:
输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict_ = {}
        half_l = len(nums)//2
        for num in nums:
            if num not in dict_:
                dict_[num] = 0
            dict_[num] += 1
            if dict_[num]>half_l:
                return num
