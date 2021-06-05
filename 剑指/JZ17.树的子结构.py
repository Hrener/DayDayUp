#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

示例1
输入：{8,8,#,9,#,2,#,5},{8,9,#,2}
返回值：true
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        # pRoot2与pRoot1中每一个节点代表的树作比较
        return self.tree(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)

    def tree(self, root1, root2):
        if not root2: # root2遍历完代表全部节点相同
            return True
        if not root1: # root1遍历完,而root2没遍历完，两者不相同
            return False
        if root1.val == root2.val:
            return self.tree(root1.left, root2.left) and self.tree(root1.right, root2.right)
        else:
            return False
