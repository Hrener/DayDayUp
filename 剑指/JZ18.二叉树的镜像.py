#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

操作给定的二叉树，将其变换为源二叉树的镜像。
比如：    源二叉树
            8
           /  \
          6   10
         / \  / \
        5  7 9 11
        镜像二叉树
            8
           /  \
          10   6
         / \  / \
        11 9 7  5

示例1
输入：{8,6,10,5,7,9,11}
返回值：{8,10,6,11,9,7,5}
"""


class Solution:
    def Mirror(self , pRoot ):
        # write code here
        def tree(root):
            if not root:
                return
            root.left, root.right = root.right, root.left
            tree(root.left)
            tree(root.right)
        tree(pRoot)
        return pRoot
