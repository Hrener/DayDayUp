#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。

示例1
输入：[3,32,321]
返回值："321323"
"""

"""
* 解题思路：
 * 先将整型数组转换成String数组，然后将String数组排序，最后将排好序的字符串数组拼接出来。关键就是制定排序规则。
 * 排序规则如下：
 * 若ab > ba 则 a > b，
 * 若ab < ba 则 a < b，
 * 若ab = ba 则 a = b；
 * 解释说明：
 * 比如 "3" < "31"但是 "331" > "313"，所以要将二者拼接起来进行比较
"""


class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        for i in range(len(numbers)-1):
            for j in range(len(numbers)-i-1):
                xishu1 = 10**len(str(numbers[j+1]))
                xishu2 = 10**len(str(numbers[j]))
                num_1 = numbers[j] * xishu1 + numbers[j+1]
                num_2 = numbers[j+1] * xishu2 + numbers[j]
                if num_1 > num_2:
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
        return "".join(map(str, numbers))
