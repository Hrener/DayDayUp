#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren
"""
描述:

输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

示例1
输入：[1,2,3,4,5,6,7],[3,2,4,1,6,5,7]
返回值：{1,2,5,3,4,6,7}
"""

"""
思路：
因为是树的结构，一般都是用递归来实现。
用数学归纳法的思想就是，假设最后一步，就是root的左右子树都已经重建好了，那么我只要考虑将root的左右子树安上去即可。

深度优先搜索：
找到先序的第一个数即为根节点，则在中序list里面根节点之前的数为左子树，之后的为右子树。
递归：创建当前根节点，并将其左子树与右子树进行递归
      1.当子树数目为空时，即当前根节点为叶子结点，无子树，返回None
      2.当子树数目为1时，即当前根节点只有一层叶子结点，返回其叶子结点
      3.当子树数目大于1时，即当前根节点有子树，创建子树的根节点，并递归子树根节点的左子树和右子树
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        else:
            res = TreeNode(pre[0])
            res.left = self.reConstructBinaryTree(pre[1:1+tin.index(pre[0])], tin[:tin.index(pre[0])])
            res.right = self.reConstructBinaryTree(pre[tin.index(pre[0])+1:], tin[tin.index(pre[0])+1:])
        return res
