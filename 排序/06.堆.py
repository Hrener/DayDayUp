"""
典型应用场景：给定一个无序数组，要求找出前 k 个最大数
"""


def maxtree(nums, nums_len, parent_idx):
    child_idx = 2*parent_idx+1
    tem = nums[parent_idx]
    while child_idx < nums_len:
        if child_idx+1 < nums_len and nums[child_idx+1] > nums[child_idx]:
            child_idx += 1
        if tem > nums[child_idx]:
            break
        nums[parent_idx], parent_idx = nums[child_idx], child_idx
        child_idx = 2*parent_idx+1
    nums[parent_idx] = tem


def sort(nums):
    n = len(nums)
    for i in range((n-2)//2, -1, -1):
        maxtree(nums, n, i)
    for end in range(n-1, 0, -1):
        nums[end], nums[0] = nums[0], nums[end]
        maxtree(nums, end, 0)


nums = [8, 7, 2, 3, 6, 1, 9, 5, 4, 0, 5]
sort(nums)
print(nums)