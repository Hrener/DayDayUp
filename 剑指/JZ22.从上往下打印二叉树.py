#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

从上往下打印出二叉树的每个节点，同层节点从左至右打印。

示例1
输入：{5,4,#,3,#,2,#,1}
返回值：[5,4,3,2,1]
"""

"""
思路：
    递归实现层序遍历。
    遍历上层节点list，保存其val到结果，并储存当前层所有节点，作为下次递归输入。
"""


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        def tree(pre_root):
            if not pre_root:
                return
            cur_root = []
            for pre in pre_root:
                self.res.append(pre.val)
                if pre.left:cur_root.append(pre.left)
                if pre.right:cur_root.append(pre.right)
            tree(cur_root)
        if not root:
            return []
        self.res = []
        tree([root])
        return self.res
