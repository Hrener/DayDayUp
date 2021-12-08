#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren

# while True:
#     try:
#         n = int(input())
#         flag = int(input())
#         data = []
#
#         for _ in range(n):
#             name, score = input().split()
#             data.append([name, int(score)])
#         for i in range(len(data)-1):
#             for j in range(len(data)-i-1):
#                 if data[j][1] > data[j+1][1]:
#                     data[j], data[j+1] = data[j+1], data[j]
#         print(data)
#         if flag == 0:data = data[::-1]
#         for d in data:
#             print(" ".join(map(str, d)))
#     except:
#         break


def quicksort(nums, left, right):
    if left >= right:return
    base, l, r = nums[left], left, right
    while l < r:
        while l < r and nums[r] >= base:
            r -= 1
        nums[l] = nums[r]
        while l < r and nums[l] <= base:
            l += 1
        nums[r] = nums[l]
    nums[l] = base
    quicksort(nums, left, l-1)
    quicksort(nums, l+1, right)


nums = [8, 7, 2, 3, 6, 1, 9, 5, 4, 0, 5]
quicksort(nums, 0, len(nums)-1)
print(nums)