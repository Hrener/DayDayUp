#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则返回true,否则返回false。假设输入的数组的任意两个数字都互不相同。（ps：我们约定空树不是二叉搜素树）

示例1
输入：[4,8,6,12,16,14,10]
返回值：true
"""

"""
思路：
    已知条件：后序序列最后一个值为root；二叉搜索树左子树值都比root小，右子树值都比root大。
    1、确定root，遍历序列（除去root结点），找到第一个大于root的位置，则该位置左边为左子树，右边为右子树；
    2、遍历右子树，若发现有小于root的值，则直接返回false；
    3、分别判断左子树和右子树是否仍是二叉搜索树（即递归步骤1、2）。
"""

class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        def tree(s):
            if len(s) <= 2:
                return
            # 1、确定root，遍历序列（除去root结点），找到第一个大于root的位置，则该位置左边为左子树，右边为右子树；
            for i in range(len(s)-1):
                if s[i] > s[-1]:
                    break
                # 处理全部小于root结点的情况
                if i == len(s) - 2:
                    i = i + 1
            left = s[:i]
            right = s[i:-1]
            # 2、遍历右子树，若发现有小于root的值，则直接返回false；
            if right and min(right) < s[-1]:
                self.res = False
                return
            # 3、分别判断左子树和右子树是否仍是二叉搜索树（即递归步骤1、2）。
            tree(left)
            tree(right)

        if not sequence:
            return False
        self.res = True
        tree(sequence)
        return self.res
