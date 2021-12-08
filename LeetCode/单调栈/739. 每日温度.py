#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren
"""
请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
"""

"""
具体操作如下：

遍历整个数组，如果栈不空，且当前数字大于栈顶元素，那么如果直接入栈的话就不是 递减栈 ，所以需要取出栈顶元素，
由于当前数字大于栈顶元素的数字，而且一定是第一个大于栈顶元素的数，直接求出下标差就是二者的距离。
继续看新的栈顶元素，直到当前数字小于等于栈顶元素停止，然后将数字入栈，这样就可以一直保持递减栈，
且每个数字和第一个大于它的数的距离也可以算出来。
"""

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0]*len(T)
        stack = []
        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                idx = stack.pop()
                res[idx] = i-idx
            stack.append(i)
        return res


# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         for i in range(len(temperatures)):
#             wait_day = 0
#             wait_idx = i
#             while wait_idx < len(temperatures) and temperatures[wait_idx] <= temperatures[i]:
#                 wait_idx += 1
#                 wait_day += 1
#             temperatures[i] = wait_day if wait_idx < len(temperatures) else 0
#         return temperatures

