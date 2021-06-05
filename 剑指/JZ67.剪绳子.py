#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:
给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1，m<=n），每段绳子的长度记为k[1],...,k[m]。
请问k[1]x...xk[m]可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

输入描述：
输入一个数n，意义见题面。（2 <= n <= 60）
返回值描述：输出答案。

示例1
输入：8
返回值：18
"""


class Solution:
    def cutRope(self, number):
        # write code here
        #可见每次分为3或2可能最佳
        # m段至少为2，>1
        if number == 2:
            return 1
        if number == 3:
            return 2
        if number == 4:
            return 4
        if number % 3 ==0:
            return pow(3,number/3)
        else:
            first = pow(3,number//3)
            second = number % 3
            # 如果余数为1，说明最后一根绳子是1，不允许,让出一根3变为4*4
            if second == 1:
                return first/3 * 2 * 2
            # 否则余数相乘即可，比如: 8 //3 = 2, 8%3 =2
            else:
                return first * second

