def maxEnvelopes(envelopes) -> int:
    l = sorted(envelopes, key=lambda x: (x[0], x[1]))
    print(l)
    curr_max = l[0]
    count_one = 1
    for i in range(1, len(l)):
        if curr_max[0] < l[i][0] and curr_max[1] < l[i][1]:
            curr_max = tuple(l[i])
            count_one += 1

    l = sorted(envelopes, key=lambda x: (x[1], x[0]))
    print(l)
    curr_max = l[0]
    count_two = 1
    for i in range(1, len(l)):
        if curr_max[0] < l[i][0] and curr_max[1] < l[i][1]:
            count_two += 1
        curr_max = tuple(l[i])

    return max(count_one, count_two)

print(maxEnvelopes([[46,89],[50,53],[52,68],[72,45],[77,81]]))