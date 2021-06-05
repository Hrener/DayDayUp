#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。

示例1
输入：{8,6,10,5,7,9,11}
返回值：[[8],[10,6],[5,7,9,11]]
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
        def dfs(pre_layer, flag):
            if not pre_layer:
                return
            tem = []
            cur_layer = []
            for root in pre_layer:
                tem.append(root.val)
                if root.left:cur_layer.append(root.left)
                if root.right:cur_layer.append(root.right)
            if not flag:
                self.res.append(tem)
            else:
                self.res.append(tem[::-1])
            dfs(cur_layer, not flag)
        if not pRoot:
            return []
        self.res = []
        dfs([pRoot], False) # 在层序遍历打印的基础上加入Flag，以判断是否逆序输出
        return self.res

