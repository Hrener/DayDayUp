#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

给定一棵二叉搜索树，请找出其中的第k小的TreeNode结点。

示例1
输入：{5,3,7,2,4,6,8},3
返回值：{4}
说明：按结点数值大小顺序第三小结点的值为4
"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        # 中序遍历存结果，最后输出第k个节点
        def tree(root):
            if not root:
                return
            tree(root.left)
            self.res.append(root)
            tree(root.right)
        self.res = []
        tree(pRoot)
        if k - 1 >= len(self.res) or k - 1 < 0:     # k-1即为第k个节点，若k不合理返回None
            return None
        return self.res[k - 1]

