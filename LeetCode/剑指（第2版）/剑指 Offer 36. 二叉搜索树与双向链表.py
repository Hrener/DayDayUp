#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren
"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。

我们希望将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。
对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。
特别地，我们希望可以就地完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，
树中节点的右指针需要指向后继。还需要返回链表中的第一个节点的指针。
"""

# class Solution:
#     def treeToDoublyList(self, root: 'Node') -> 'Node':
#         def tree(root):
#             if not root:
#                 return
#             tree(root.left)
#             self.li.append(root)
#             tree(root.right)
#         if not root:return
#         self.li = []
#         tree(root)
#         self.li.append(self.li[0])
#         for i in range(len(self.li)-1):
#             self.li[i].right = self.li[i+1]
#             self.li[i+1].left = self.li[i]
#         return self.li[0]

class Solution:
    def __init__(self):
        self.res = None
        self.pre = None
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def tree(root):
            if not root:
                return
            tree(root.left)
            if not self.pre:
                self.res = self.pre = root
            else:
                self.pre.right = root
                root.left = self.pre
                self.pre = root
            tree(root.right)
        if not root:return
        tree(root)
        self.res.left, self.pre.right = self.pre, self.res
        return self.res
