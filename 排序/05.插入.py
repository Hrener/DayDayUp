"""
插入排序是一种简单直观的排序算法。它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。

算法描述
把待排序的数组分成已排序和未排序两部分，初始的时候把第一个元素认为是已排好序的。
从第二个元素开始，在已排好序的子数组中寻找到该元素合适的位置并插入该位置。
重复上述过程直到最后一个元素被插入有序子数组中。
"""


def sort(nums):
    res = []
    for num in nums:
        idx = 0
        while idx < len(res) and num > res[idx]:
            idx += 1
        res.insert(idx, num)
    return res


nums = [8, 7, 2, 3, 6, 1, 9, 5, 4, 0, 5]
print(sort(nums))