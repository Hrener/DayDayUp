#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。

示例 :
给定二叉树
          1
         / \
        2   3
       / \
      4   5
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
"""

# 双重递归（耗时），自顶向下
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:return 0
            left = dfs(root.left)
            right = dfs(root.right)
            return max(left, right) + 1
        if not root:return 0
        l = dfs(root.left) + dfs(root.right)
        return max(l, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

# 递归：自低向上
#       计算二叉树中每个节点的 （左子树 与 右子树 的 深度 之和，即left+right）
#       最终二叉树的直径就是 二叉树中每个节点的深度之和 的最大值
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.res = max(self.res, left+right)
            return max(left, right) + 1
        if not root:return 0
        self.res = 0
        dfs(root)
        return self.res
