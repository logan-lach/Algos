
def func(nums):
    hold = set()

    for i in range(len(nums)):
        if i in hold:
            return [nums[i], nums[i] + 1]
        hold.add(nums[i])

print(func([2,2]))