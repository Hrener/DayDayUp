#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。
不能使用除法。（注意：规定B[0] = A[1] * A[2] * ... * A[n-1]，B[n-1] = A[0] * A[1] * ... * A[n-2];）
对于A长度为1的情况，B无意义，故而无法构建，因此该情况不会存在。

示例1
输入：[1,2,3,4,5]
返回值：[120,60,40,30,24]
"""


class Solution:
    def multiply(self, A):
        # write code here
        B = []
        for i in range(len(A)):
            tem = 1
            for j in range(len(A)):
                if i == j:
                    continue
                tem *= A[j]
            B.append(tem)
        return B
