#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。要求时间复杂度为 O(n).

示例1
输入：[1,-2,3,10,-4,7,2,-5]
返回值：18
说明：
输入的数组为{1,-2,3,10,—4,7,2,一5}，和最大的子数组为{3,10,一4,7,2}，因此输出为该子数组的和 18。
"""

"""
思路一:
    动态规划
    dp[i]表示以元素array[i]结尾的最大连续子数组和.
    以[-2,-3,4,-1,-2,1,5,-3]为例，可以发现,
        dp[0] = -2
        dp[1] = -3
        dp[2] = 4
        dp[3] = 3
    以此类推,会发现
        dp[i] = max{dp[i-1]+array[i],array[i]}.
"""


class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        n = len(array)
        dp = [i for i in array]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + array[i], array[i])

        return max(dp)


"""
思路二：
    初始化最大值，遍历积累，最大值取（最大值，临时积累的最大值）中的较大值，若临时积累的最大值小于零，重新积累
"""


class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        res = array[0]  # 不能初始为0，存在负数
        tem = 0
        for i in range(len(array)):
            tem += array[i]
            res = max(res, tem)
            if tem < 0:
                tem = 0
        return res

