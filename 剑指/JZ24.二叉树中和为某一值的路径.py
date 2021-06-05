#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren


"""
描述:

输入一颗二叉树的根节点和一个整数，按字典序打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。

示例1
输入：{10,5,12,4,7},22
返回值：[[10,5,7],[10,12]]
示例2
输入：{10,5,12,4,7},15
返回值：[]
"""

"""
思路：
    深度优先搜索。
    深度优先搜索由根节点开始到叶子结点的每一个路径。
        1. 当前节点不是叶子节点时，若此时路径的val和小于目标整数时，继续向下搜索，否则停止搜索。
        2. 当前节点是叶子节点时，若此时路径的val和等于目标整数时，搜索成功保存路径val的list，否则搜索失败不保存
"""


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        self.res = []
        self.expectNumber = expectNumber
        def dfs(root, sum_list):
            if not root:
                return
            # 这里要注意，如果用append进行添加那么sum_list的地址永远是不变的，因此要用加号，得到的sum_list的地址是新的
            sum_list = sum_list + [root.val]
            if not root.left and not root.right:
                if sum(sum_list) == self.expectNumber:
                    self.res.append(sum_list)
            else:
                if sum(sum_list) < self.expectNumber:
                    dfs(root.left, sum_list)
                    dfs(root.right, sum_list)
        dfs(root, [])
        return self.res


a = [1]
print(id(a))    # 1823568961032
a.append(2)
print(id(a))    # 1823568961032
a = a + [2]
print(id(a))    # 1823567243464

# 因此递归时，若要使用list,不要用append()要用加号
