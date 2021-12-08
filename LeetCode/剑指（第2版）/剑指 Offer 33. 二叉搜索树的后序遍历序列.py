#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren
"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

参考以下这颗二叉搜索树：
     5
    / \
   2   6
  / \
 1   3

示例 1：
输入: [1,6,3,2,5]
输出: false

示例 2：
输入: [1,3,2,6,5]
输出: true
"""


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
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

        if not postorder:
            return True
        self.res = True
        tree(postorder)
        return self.res
