#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述:

输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
"""

"""
思路：
    中序遍历，首先复制一个头结点作为双向链表的一端，
    遍历过程中：
        1. 将上一个节点的right指向当前节点
        2. 将当前节点的left指向上一个节点
        3. 将当前节点作为上一个节点
"""


class Solution:
    def __init__(self):
        self.before = None
        self.head = None

    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return None
        self.Convert(pRootOfTree.left)
        if not self.before:
            self.before = pRootOfTree
            self.head = pRootOfTree
        else:
            self.before.right = pRootOfTree # 上一个节点的right指向当前节点
            pRootOfTree.left = self.before  # 当前节点的left指向上一个节点
            self.before = pRootOfTree       # 当前节点作为上一个节点
        self.Convert(pRootOfTree.right)
        return self.head


class Solution:
    def Convert(self, pRootOfTree):
        # write code here

        def tree(root):
            if not root:
                return
            tree(root.left)
            self.mid_sort.append(root)
            tree(root.right)

        if not pRootOfTree:
            return
        self.mid_sort = []
        tree(pRootOfTree)
        for i in range(len(self.mid_sort) - 1):
            self.mid_sort[i].right = self.mid_sort[i + 1]
            self.mid_sort[i + 1].left = self.mid_sort[i]
        return self.mid_sort[0]
