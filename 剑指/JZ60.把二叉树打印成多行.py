#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
示例1
输入：{8,6,10,5,7,9,11}
返回值：[[8],[6,10],[5,7,9,11]]
"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        def dfs(pre_layer):
            if not pre_layer:
                return
            tem = []
            cur_layer = []
            for root in pre_layer:
                tem.append(root.val)
                if root.left:cur_layer.append(root.left)
                if root.right:cur_layer.append(root.right)
            self.res.append(tem)
            dfs(cur_layer)
        if not pRoot:
            return []
        self.res = []
        dfs([pRoot])
        return self.res
