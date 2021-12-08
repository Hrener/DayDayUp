#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
给你二叉树的根结点 root ，请你将它展开为一个单链表：
展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
展开后的单链表应该与二叉树 先序遍历 顺序相同。
 
示例 1：
输入：root = [1,2,5,3,4,null,6]
输出：[1,null,2,null,3,null,4,null,5,null,6]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [0]
输出：[0]
"""


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.Node = []
        def dfs(root):
            if not root:
                return
            self.Node.append(root)
            dfs(root.left)
            dfs(root.right)
        if not root:return []
        dfs(root)
        for i in range(len(self.Node)-1):
            self.Node[i].left = None
            self.Node[i].right = self.Node[i+1]
