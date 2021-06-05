#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）

示例1
输入：[1,2,3,4,5],[4,3,5,1,2]
返回值：false
"""

"""
思路：
    借用一个辅助list进行复盘。
    遍历pushV存入辅助list，直到辅助list的末端 等于 popV的头端
    之后再删除 辅助list的末端 以及 popV的头端，直到两者不相等
    然后当遍历结束之后，辅助list应该为空，因此返回False, 否则返回True
"""


class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        fupan = []
        for push_i in range(len(pushV)):
            fupan.append(pushV[push_i])
            while fupan[-1] == popV[0]:
                fupan.pop(-1)
                popV.pop(0)
                if not fupan:
                    break
            if push_i == len(pushV)-1 and len(fupan):
                return False
        return True
