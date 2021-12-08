#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren
"""
输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

例如：
给定二叉树 [3,9,20,null,null,15,7]，
    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
"""


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(pre_layer):
            if not pre_layer:return
            self.res += 1
            cur = []
            for pre in pre_layer:
                if pre.left:cur.append(pre.left)
                if pre.right:cur.append(pre.right)
            dfs(cur)
        if not root:return 0
        self.res = 0
        dfs([root])
        return self.res


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right)+1
