#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren
"""
找出数组中重复的数字。
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，
也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：
输入：[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3
"""

# 方法一: （60ms）
#     哈希
#     复杂度分析：
#     时间复杂度 O(N)：遍历数组使用 O(N)，HashSet 添加与查找元素皆为 O(1)。
#     空间复杂度 O(N)：HashSet占用 O(N)大小的额外空间。
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        dict_ = {}
        for num in nums:
            if num not in dict_:
                dict_[num] = 0
            dict_[num] += 1
            if dict_[num] > 1:
                return num

# 方法二：(48ms)
#     1.将遍历到的元素绝对值作为索引下标，若索引到的值为负，返回元素绝对值，否则将索引到的值乘-1
#     2.不过要单独考虑0的情况
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        if nums.count(0)>1:return 0
        for num in nums:
            if nums[abs(num)] < 0:
                return abs(num)
            nums[num] *= -1

# 方法三：(48ms)
#     1. 排序
#     2.相邻元素相等则代表重复，返回
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]
