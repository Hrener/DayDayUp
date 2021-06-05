#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。
现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!

返回值描述：
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序

示例1
输入：9
返回值：[[2,3,4],[4,5]]
"""

"""
思路：
    双指针
"""


class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        # 至少包括两个数, tsum小于等于2时直接返回[]
        if tsum <= 2:
            return []

        self.res = []
        ts = [i for i in range(1, tsum//2+2)]   # 输入：9，遍历list为[1, 2, 3, 4, 5]
        left = 0
        while left < len(ts):
            right = left + 1
            while right <= len(ts):
                tem = sum(ts[left:right])
                if tem == tsum:
                    self.res.append(ts[left:right])
                right += 1
            left += 1
        return self.res
