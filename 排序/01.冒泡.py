#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Hren


def sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


nums = [8, 7, 2, 3, 6, 1, 9, 5, 4, 0]
print(sort(nums))
