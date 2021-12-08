
# def sort(nums):
#     length = len(nums)
#     dist = length // 2
#
#     while dist > 0:
#         for i in range(dist, length):
#             temp = nums[i]
#             j = i
#             while j >= dist and temp < nums[j - dist]:
#                 nums[j] = nums[j - dist]
#                 j -= dist
#             nums[j] = temp
#         dist //= 2


def sort(nums):
    dist = len(nums)//2

    while dist > 0:
        for i in range(dist, len(nums)):
            j = i
            tem = nums[i]
            # 找到比tem大的位置，插入tem,其他后移
            while j >= dist and tem < nums[j-dist]:
                nums[j] = nums[j-dist]
                j -= dist
            nums[j] = tem
        dist //= 2


nums = [8, 7, 2, 3, 6, 1, 9, 5, 4, 0, 5]
sort(nums)
print(nums)