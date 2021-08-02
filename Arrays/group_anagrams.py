def groupAnagrams(strs):
    seen_strings = set()
    holder = dict()
    for i in strs:
        temp = ''.join(sorted(i))
        if temp in seen_strings:
            holder[temp] += [i]
        else:
            holder[temp] = [i]
            seen_strings.add(temp)
    return holder.values

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))