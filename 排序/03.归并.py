#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren


# def split(nums):
#     if len(nums) == 1:return nums
#     idx = len(nums)//2
#     s1, s2 = nums[:idx], nums[idx:]
#     return merge(split(s1), split(s2))
#
#
# def merge(s1, s2):
#     tem = []
#     idx1, idx2 = 0, 0
#     while idx1 < len(s1) and idx2 < len(s2):
#         if s1[idx1] < s2[idx2]:
#             tem.append(s1[idx1])
#             idx1 += 1
#         else:
#             tem.append(s2[idx2])
#             idx2 += 1
#     if idx1 == len(s1):
#         tem = tem + s2[idx2:]
#     else:
#         tem = tem + s1[idx1:]
#     return tem


def split(nums):
    if len(nums) < 2:return nums
    mid = len(nums)//2
    a = split(nums[:mid])
    b = split(nums[mid:])
    return merge(a, b)


def merge(a, b):
    a_idx, b_idx = 0, 0
    res = []
    while a_idx < len(a) and b_idx < len(b):
        if a[a_idx] < b[b_idx]:
            res.append(a[a_idx])
            a_idx += 1
        else:
            res.append(b[b_idx])
            b_idx += 1
    return res+b[b_idx:] if a_idx == len(a) else res+a[a_idx:]


nums = [8, 7, 2, 3, 6, 1, 9, 5, 4, 0, 5]
print(split(nums))