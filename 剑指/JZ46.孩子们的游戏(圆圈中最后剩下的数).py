#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

"""
描述
每年六一儿童节,牛客都会准备一些小礼物去看望孤儿院的小朋友,今年亦是如此。HF作为牛客的资深元老,自然也准备了一些小游戏。
其中,有个游戏是这样的:首先,让小朋友们围成一个大圈。然后,他随机指定一个数m,让编号为0的小朋友开始报数。
每次喊到m-1的那个小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,并且不再回到圈中,
从他的下一个小朋友开始,继续0...m-1报数....这样下去....直到剩下最后一个小朋友,可以不用表演,
并且拿到牛客名贵的“名侦探柯南”典藏版(名额有限哦!!^_^)。请你试着想下,哪个小朋友会得到这份礼品呢？
(注：小朋友的编号是从0到n-1)

如果没有小朋友，请返回-1
示例1
输入：5,3
返回值：3
"""

"""
思路一（慢）：
    如果m % 当前圆圈周长大于零：pop_idx = m % len(circle)-1，否则pop_idx = len(circle)-1。
    切片将否则pop_idx后的元素，放于前面
思路二（快）：
    pop_idx = (上次的pop_idx + m - 1) % 当前圆圈周长
    从circle弹出pop_idx元素
"""


class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if not n:return -1
        circle = [i for i in range(n)]
        while len(circle) > 1:
            pop_idx = m % len(circle)-1 if m % len(circle) > 0 else len(circle)-1
            circle = circle[pop_idx+1:] + circle[:pop_idx]
        return circle[0]


class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if not n:return -1
        circle = [i for i in range(n)]
        idx = 0
        while len(circle) > 1:
            pop_idx = (idx + m - 1) % len(circle)
            circle.pop(pop_idx)
            idx = pop_idx
        return circle[0]
