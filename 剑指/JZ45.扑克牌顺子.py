#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

现在有2副扑克牌，从扑克牌中随机五张扑克牌，我们需要来判断一下是不是顺子。有如下规则：
1. A为1，J为11，Q为12，K为13，A不能视为14
2. 大、小王为 0，0可以看作任意牌
3. 如果给出的五张牌能组成顺子（即这五张牌是连续的）就输出true，否则就输出false。
例如：给出数据[6,0,2,0,4]
中间的两个0一个看作3，一个看作5 。即：[6,3,2,5,4]
这样这五张牌在[2,6]区间连续，输出true
数据保证每组5个数字，每组最多含有4个零，数组的数取值为 [0, 13]

示例1
输入：[6,0,2,0,4]
返回值：true
示例2
输入：[0,3,2,6,4]
返回值：true
示例3
输入：[1,0,0,1,0]
返回值：false
示例4
输入：[13,12,11,0,1]
返回值：false
"""

"""
思路：
    取出非零扑克牌：
        若点数数目 小于 非零扑克牌数目， 即存在相同扑克牌，返回False
        若非零扑克牌只有一张，返回True
        若非零扑克牌多于一张，如果最大值与最小值的差值 大于 4，返回False, 否则返回True
"""



class Solution:
    def IsContinuous(self, numbers):
        # write code here
        no_zero = []
        for num in numbers:
            if num:no_zero.append(num)
        if len(set(no_zero)) < len(no_zero):
            return False
        if len(no_zero) == 1:
            return True
        else:
            if max(no_zero) - min(no_zero) > 4:
                return False
            return True

