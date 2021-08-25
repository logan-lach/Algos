def searchRange(nums,target):
    start = 0
    end = len(nums) - 1
    found_index = -1
    coords = []

    while start < end - 1:
        mid = (start + end) // 2

        if nums[mid] < target:
            start = mid
        elif nums[mid] > target:
            end = mid

        elif nums[mid] == target:
            found_index = mid
            break

    if found_index == -1:
        if nums[start] == target:
            found_index = start
        elif nums[end] == target:
            found_index = end
        else:
            return [-1, -1]

    coords = [found_index, found_index]

    start = 0
    end = found_index

    while start < end - 1:
        mid = (start + end) // 2
        if nums[mid] < target:
            start = mid
        elif nums[mid] == target:
            end = mid

    if nums[start] == target:
        coords[0] = start
    elif nums[end] == target:
        coords[0] = end

    start = 0
    end = found_index

    while start < end - 1:
        mid = (start + end) // 2
        if nums[mid] > target:
            end = mid
        elif nums[mid] == target:
            start = mid
    if nums[end] == target:
        coords[1] = end
    elif nums[start] == target:
        coords[1] = start
    return coords



print(searchRange([5,7,7,8,8,10], 8))
