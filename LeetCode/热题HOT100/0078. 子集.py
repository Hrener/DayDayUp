#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

示例 1：
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

示例 2：
输入：nums = [0]
输出：[[],[0]]

提示：
    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
    nums 中的所有元素 互不相同
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def dfs(tem, n, num):
            if len(tem)==n:
                if tem not in self.res:
                    self.res.append(tem)
                return
            for i in range(len(num)):
                dfs(tem + [num[i]], n, num[i+1:])
        for i in range(len(nums)+1):
            dfs([], i, nums)
        return self.res


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def dfs(tem,nums):
            self.res.append(tem)
            for i in range(len(nums)):
                dfs(tem + [nums[i]],nums[i+1:])
        dfs([],nums)
        return self.res
