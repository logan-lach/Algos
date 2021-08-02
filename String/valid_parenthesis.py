def isValid(s: str) -> bool:
    matches = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    start = 0
    queue = [s[0]]

    for i in range(1, len(s)):
        if s[i] in matches.keys():
            queue.append(i)
        else:
            if matches[queue[start]] == s[i]:
                start += 1
            else:
                return False
    return start == len(queue)

print(isValid("()[]{}"))