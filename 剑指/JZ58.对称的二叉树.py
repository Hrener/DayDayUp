#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

请实现一个函数，用来判断一棵二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。

示例1
输入：{8,6,6,5,7,7,5}
返回值：true
示例2
输入：{8,6,9,5,7,7,5}
返回值：false
"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True

        def digui(pleft, pright):
            # 若左右对称位置pleft和pright均为None，return True
            if (not pleft) and (not pright):
                return True
            # 若左右对称位置pleft和pright中只有一个为None，return False
            if (not pleft) or (not pright):
                return False
            # 若左右对称位置pleft和pright的val不相等，return False
            if pleft.val != pright.val:
                return False
            return digui(pleft.left, pright.right) and digui(pleft.right, pright.left)

        return digui(pRoot.left, pRoot.right)

