def lengthOfLongestSubstring( s: str) -> int:
    seen = set()

    ptr = 0
    maximum = 0

    for i in range(len(s)):
        if s[i] in seen:
            maximum = max(maximum, i - ptr)
            while ptr < len(s) and s[ptr] != s[i]:
                seen.remove(s[ptr])
                ptr += 1
            ptr += 1

        else:
            seen.add(s[i])

    maximum = max(maximum, len(s) - ptr)
    return maximum


print(lengthOfLongestSubstring("dvdf"))