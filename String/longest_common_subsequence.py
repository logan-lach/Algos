def lcs(text1, text2):
    arr = [[0 for i in range(len(text1) + 1)] for j in range(len(text2) + 1)]

    curr_max = 0
    for row in range(1, len(text2) + 1):
        for col in range(1, len(text1) + 1):
            if text1[col - 1] == text2[row - 1]:
                arr[row][col] = arr[row - 1][col - 1] + 1
                curr_max = max(curr_max, arr[row][col])
            else:
                arr[row][col] = max(arr[row - 1][col], arr[row][col - 1])

    return curr_max