#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

示例1
输入：7
返回值：8
"""


# 超时
'''class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        res = 0
        res_list = []
        idx = 1
        while idx:
            n = idx
            while n:
                for i in [5, 3, 2]:
                    while n % i == 0:
                        n = n // i
                        if n in res_list:
                            n = 1
                            break
                if n == 1:
                    res += 1
                    res_list.append(idx)
                break
            if res == index:
                return idx
            idx += 1'''


class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        '''
        思路1.暴力法  需要遍历所有数，o(n^2)复杂度，超时。
        思路2.暴力+存储  也需要遍历所有数，只是反证丑数时节约时间，o(n^2)复杂度，依旧超时。
        思路3.存储最小丑数，依次向上取，o(n)复杂度。
        '''
        if index <= 1:
            return index
        res = [1]* index
        i2,i3,i5 = 0,0,0
        for i in range(1,index):
            res[i] = min(res[i2]*2,res[i3]*3,res[i5]*5)
            if res[i] == res[i2]*2:
                i2 += 1
            if res[i] == res[i3]*3:
                i3 += 1
            if res[i] == res[i5]*5:
                i5 += 1
        return res[-1]
