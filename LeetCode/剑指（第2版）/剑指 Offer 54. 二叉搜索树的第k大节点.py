#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren
"""
给定一棵二叉搜索树，请找出其中第k大的节点。

示例 1:
输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4

示例 2:
输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4
限制：1 ≤ k ≤ 二叉搜索树元素个数
"""

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def kthLargest(self, root: TreeNode, k: int) -> int:
#         def tree(root):
#             if not root:return
#             tree(root.left)
#             self.res.append(root.val)
#             tree(root.right)
#         if not root:return
#         self.res = []
#         tree(root)
#         return self.res[-k]

class Solution:
    def __init__(self):
        self.i = 0
    def kthLargest(self, root: TreeNode, k: int) -> int:
        if not root:return 0
        r = self.kthLargest(root.right, k)
        self.i += 1
        if self.i == k:
            return root.val
        l = self.kthLargest(root.left, k)
        return max(r, l)
