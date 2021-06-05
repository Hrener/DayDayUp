#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则按字典序打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
输入描述：输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。

示例1
输入："ab"
返回值：["ab","ba"]
"""

"""
思路：
    递归是一种算法结构，回溯是一种算法思想
一个递归就是在函数中调用函数本身来解决问题
    回溯就是通过不同的尝试来生成问题的解，有点类似于穷举，但是和穷举不同的是回溯会“剪枝”，
    意思就是对已经知道错误的结果没必要再枚举接下来的答案了，比如一个有序数列1,2,3,4,5，我要找和为5的所有集合，
    从前往后搜索我选了1，然后2，然后选3 的时候发现和已经大于预期，那么4,5肯定也不行，这就是一种对搜索过程的优化

回溯搜索是深度优先搜索（DFS）的一种
    对于某一个搜索树来说（搜索树是起记录路径和状态判断的作用），回溯和DFS，其主要的区别是，
    回溯法在求解过程中不保留完整的树结构，而深度优先搜索则记下完整的搜索树。
"""

class Solution:
    def Permutation(self, ss):
        # write code here
        def dfs(s, keep):
            if len(s) == len(ss) and s not in self.res:
                self.res.append(s)
            for i in range(len(keep)):
                dfs(s+keep[i], keep[:i] + keep[i+1:])
        self.res = []
        dfs("", ss)
        return self.res
