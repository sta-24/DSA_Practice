def group_anagrams(strs):
    anagrams = defaultdict(list)
    for s in strs:
        sorted_s = ''.join(sorted(s))
        anagrams[sorted_s].append(s)
    return list(anagrams.values())