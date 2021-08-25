"""
I Got this one wrong in the interview I just had. Never let that shit happen again
"""

def num_from_str(string):

    values = [0] * 10

    for i in string:
        if i == 'z':
            values[0] += 1
        if i == 'w':
            values[2] += 1
        if i == 'f':
            values[4] += 1
        if i == 'x':
            values[6] += 1
        if i == 'g':
            values[8] += 1
        if i == 'o':
            values[1] += 1
        if i == 'h':
            values[3] += 1
        if i == 'v':
            values[5] += 1
        if i == 's':
            values[7] += 1
        if i == 'i':
            values[9] += 1


    values[7] -= values[6]
    values[5] -= values[7]
    values[4] -= values[5]
    values[1] -= (values[2] + values[4] + values[0])
    values[3] -= values[8]
    values[9] -= (values[5] + values[6] + values[8])

    string = ""
    for i in range(len(values)):
        string += str(i) * values[i]

    return string

print(num_from_str("owoftnuoer"))

