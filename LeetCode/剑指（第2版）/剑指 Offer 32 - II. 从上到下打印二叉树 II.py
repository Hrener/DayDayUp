#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren
"""
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。
例如:
给定二叉树: [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：
[
  [3],
  [9,20],
  [15,7]
]
"""

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def dfs(pre_layer):
            if not pre_layer:return
            cur = []
            tem_val = []
            for pre in pre_layer:
                tem_val.append(pre.val)
                if pre.left:cur.append(pre.left)
                if pre.right:cur.append(pre.right)
            self.res.append(tem_val)
            dfs(cur)
        if not root:return []
        self.res = []
        dfs([root])
        return self.res
