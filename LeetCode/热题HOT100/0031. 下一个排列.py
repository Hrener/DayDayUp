#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
必须 原地 修改，只允许使用额外常数空间。

示例 1：
输入：nums = [1,2,3]
输出：[1,3,2]

示例 2：
输入：nums = [3,2,1]
输出：[1,2,3]

示例 3：
输入：nums = [1,1,5]
输出：[1,5,1]

示例 4：
输入：nums = [1]
输出：[1]

提示：
    1 <= nums.length <= 100
    0 <= nums[i] <= 100
"""


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        min_idx = n-1
        for i in range(n-1, 0, -1):
            # 当逆序遍历遇到第一个 升序对（如[1, 3, 2]中(1, 3)）时，进行修改
            if nums[i] > nums[i-1]:
                # 将（i-1之后的最小 且 比i-1大）的值 与 （i-1）的值 进行交换
                while nums[min_idx] <= nums[i-1]:
                    min_idx -= 1
                nums[min_idx], nums[i-1] = nums[i-1], nums[min_idx]
                # 将从i开始后的值进行排序（冒泡）
                for m in range(0, n-i-1):
                    for j in range(0, n-m-i-1):
                        if nums[i+j] > nums[i+j+1]:
                            nums[i+j], nums[i+j+1] = nums[i+j+1], nums[i+j]
                return
        # 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
        for j in range(n//2):
            nums[j], nums[n-j-1] = nums[n-j-1], nums[j]
