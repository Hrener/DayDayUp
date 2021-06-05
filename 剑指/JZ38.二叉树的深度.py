#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。

示例1
输入：{1,2,3,4,5,#,6,#,#,7}
返回值：4
"""

"""
思路：
    递归、或 层序遍历 实现
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 1.递归一
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        self.res = []
        def dfs(root, num):
            if not root:
                self.res.append(num)
                return
            num += 1
            dfs(root.left, num)
            dfs(root.right, num)
        dfs(pRoot, 0)
        return max(self.res)


# 2.递归二，
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        return max(left, right) + 1


# 3.层序遍历
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        def tree(pre_root):
            if not pre_root:
                return
            self.res += 1
            cur_root = []
            for pre in pre_root:
                if pre.left:cur_root.append(pre.left)
                if pre.right:cur_root.append(pre.right)
            tree(cur_root)
        if not pRoot:
            return 0
        self.res = 0
        tree([pRoot])
        return self.res
