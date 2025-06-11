def our_max(nums):
    nums.sort()
    return nums[-1]

print(our_max([1, 2, 10, 9, 3, 7, 0, 99, 27, 85]))