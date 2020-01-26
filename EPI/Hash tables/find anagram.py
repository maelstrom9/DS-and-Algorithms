

import collections

def find_anagram(dictionary):

    anagrams = collections.defaultdict(list)

    for s in dictionary:
        temp = [0]*26
        for c in s:
            temp[ord(c)-ord('a')] += 1
        anagrams[tuple(temp)].append(s)  ## tuple is hashable.

    return [group for group in anagrams.values() if len(group)>=2]


print(find_anagram(["ab","ba","cdc","ccd","alex","lexa","apple","imain","inami","nigma","gamin","ginam"]))


t = collections.defaultdict(int)
print(t[10])