#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren
"""
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

例如，给出
前序遍历 preorder = [3,9,20,15,7] 中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：
    3
   / \
  9  20
    /  \
   15   7
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# （168ms）
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def dfs(root, preo, ino):
            if len(preo)==1:return
            root_idx = ino.index(root.val)
            if root_idx > 0:
                root.left = TreeNode(preo[1])
                dfs(root.left, preo[1:1+root_idx], ino[:root_idx])
            if root_idx < len(ino)-1:
                root.right = TreeNode(preo[root_idx+1])
                dfs(root.right, preo[root_idx+1:], ino[root_idx+1:])
        if not preorder:return
        root = TreeNode(preorder[0])
        dfs(root, preorder, inorder)
        return root

# （272ms）
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:return
        elif len(preorder) == 1:
            return TreeNode(preorder[0])
        else:
            root = TreeNode(preorder[0])
            root.left = self.buildTree(preorder[1:1+inorder.index(preorder[0])], inorder[:inorder.index(preorder[0])])
            root.right = self.buildTree(preorder[inorder.index(preorder[0])+1:], inorder[inorder.index(preorder[0])+1:])
        return root
