def pos(nums,target):
    if len(nums) == 1:
        return 1 if target > nums[0] else 0

    elif len(nums) == 0:
        return 0

    start = 0
    end = len(nums) - 1

    while start < end:
        mid = int((start + end) / 2)

        if target > nums[mid]:
            start = mid

        elif target < nums[mid]:
            end = mid

        else:
            return mid

    return start if nums[start] < target else start + 1

print(pos([1,3,5,6], 2))