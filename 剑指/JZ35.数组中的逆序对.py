#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述：

在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,
求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007

示例
输入：[1,2,3,4,5,6,7,0]
输出：7
"""


"""
归并排序
"""


class Solution:
    def __init__(self):
        self.out = 0

    def InversePairs(self, data):
        # write code here
        self.merge_sort(data)
        return self.out % 1000000007

    def merge_sort(self, s):
        l = len(s)
        if l < 2:
            return
        s1 = s[:l // 2]
        s2 = s[l // 2:]
        self.merge_sort(s1)
        self.merge_sort(s2)
        self.merge(s1, s2, s)

    def merge(self, s1, s2, s):
        i, j = len(s1) - 1, len(s2) - 1
        while i + j > -2:
            if i >= 0 and j >= 0:
                if s1[i] > s2[j]:
                    self.out += j + 1
                    s[i + j + 1] = s1[i]
                    i -= 1
                else:
                    s[i + j + 1] = s2[j]
                    j -= 1
            else:
                if i < 0:
                    s[i + j + 1] = s2[j]
                    j -= 1
                else:
                    s[i + j + 1] = s1[i]
                    i -= 1


a = [5, 6, 1, 2, 3, 4, 7, 0]
S = Solution()
b = S.InversePairs(a)
print(b)
print(a)
