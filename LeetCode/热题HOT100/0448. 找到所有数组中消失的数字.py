#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren
"""
给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。

示例 1：
输入：nums = [4,3,2,7,8,2,3,1]
输出：[5,6]

示例 2：
输入：nums = [1,1]
输出：[2]
 
提示：
    n == nums.length
    1 <= n <= 105
    1 <= nums[i] <= n
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 将所有正数作为数组下标，置对应数组值为负值。那么，仍为正数的位置即为（未出现过）消失的数字。
        # 原始数组：[4,3,2,7,8,2,3,1]
        # 重置后为：[-4,-3,-2,-7,8,2,-3,-1]
        # 结论：[8,2] 分别对应的index为[5,6]（消失的数字）
        res = []
        nums_ = nums
        for idx in nums_:
            nums[abs(idx)-1] = -1 * abs(nums[abs(idx)-1])
        for i in range(1, len(nums)+1):
            if nums[i-1] > 0:
                res.append(i)
        return res

