#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren
"""
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

例如:
给定二叉树: [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：
[
  [3],
  [20,9],
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
            if len(self.res)%2==1:tem_val = tem_val[::-1]
            self.res.append(tem_val)
            dfs(cur)
        if not root:return []
        self.res = []
        dfs([root])
        return self.res
