#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

输入一棵二叉树，判断该二叉树是否是平衡二叉树。
在这里，我们只需要考虑其平衡性，不需要考虑其是不是排序二叉树
平衡二叉树（Balanced Binary Tree），具有以下性质：它是一棵空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树。

注：我们约定空树是平衡二叉树。
示例1
输入：{1,2,3,4,5,6,7}
返回值：true
"""

"""
思路：
    可以看做计算二叉树深度题目的扩展：
    加一步判断：
        若left子树 与 right子树的深度差值大于1，即非平衡二叉树
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        self.res = True
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if abs(left - right) > 1:
                self.res = False
            return max(left, right) + 1
        dfs(pRoot)
        return self.res

