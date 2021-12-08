#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren
"""
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)。

示例1:
输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

提示：
1 <= arr.length <= 10^5
-100 <= arr[i] <= 100
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_value = nums[0]
        tem_value = 0
        for num in nums:
            tem_value += num
            max_value = max(max_value, tem_value)
            if tem_value<0:
                tem_value = 0
        return max_value


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]*len(nums)
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        return max(dp)
