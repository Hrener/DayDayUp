#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren
"""
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
"""


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # write code here
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        else:
            res = TreeNode(preorder[0])
            idx = inorder.index(preorder[0])
            res.left = self.buildTree(preorder[1:1+idx], inorder[:idx])
            res.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
        return res
