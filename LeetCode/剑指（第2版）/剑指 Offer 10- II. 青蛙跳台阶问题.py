#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren
"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：
输入：n = 2 输出：2

示例 2：
输入：n = 7 输出：21

示例 3：
输入：n = 0 输出：1

提示：0 <= n <= 100
"""


class Solution:
    def numWays(self, n: int) -> int:
        if n == 0:return 1
        a, b = 0, 1
        while n > 0:
            a, b = b, a+b
            b = b%(1000000007)
            n -= 1
        return b


class Solution:
    def numWays(self, n: int) -> int:
        dp = [1]+[1]*n
        for i in range(2,n+1):
            dp[i] = dp[i-2]+dp[i-1]
            dp[i] = dp[i]%(1000000007)
            n -= 1
        return dp[-1]
