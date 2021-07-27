def romanToInt( s: str) -> int:
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    value = 0

    for i in range(len(s)):

        if i < len(s) - 1 and s[i] == 'I':
            if s[i + 1] == 'V':
                value += 4
                continue
            elif s[i + 1] == 'X':
                value += 9
                continue

        elif i < len(s) - 1 and s[i] == 'X':
            if s[i + 1] == 'L':
                value += 40
                continue
            elif s[i + 1] == 'C':
                value += 90
                continue

        elif i < len(s) - 1 and s[i] == 'C':
            if s[i + 1] == 'D':
                value += 400
                continue
            elif s[i + 1] == 'M':
                value += 900
                continue

        value += roman[s[i]]
    return value

print(romanToInt('IV'))









