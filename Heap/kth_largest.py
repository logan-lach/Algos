from math import floor
def kth_largest(nums, k):
    def heapify(A):
        for i in range(int(len(A) / 2), -1, -1):
            float_down(A, i)


    def float_down(A, i):
        if i >= len(A):
            return

        left = 2 * (i) + 1
        right = 2 * (i) + 2
        largest = i

        if left < len(A) and A[left] > A[largest]:
            largest = left
        if right < len(A) and A[right] > A[largest]:
            largest = right

        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            float_down(A, largest)

    heapify(nums)
    print(nums)
    for i in range(k - 1):
        nums[0] = nums[len(nums) - 1]
        nums.pop()
        heapify(nums)

    return nums[0]

print(kth_largest([3,2,1,5,6,4],2))