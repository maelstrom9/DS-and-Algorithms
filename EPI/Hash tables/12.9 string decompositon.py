
from collections import Counter

def string_decomposition(s,words):

    if not s or not words or not words[0]:
        return []

    word_len = len(words[0])
    word_counts = Counter(words)
    res = []

    for i in range(len(s)-word_len):
        if s[i:i+word_len] not in word_counts:
            continue
        else:
            temp = {}
            j = i
            while j<len(s) and len(temp)<=len(word_counts):
                if s[j:j+word_len] not in word_counts:
                    break
                elif s[j:j+word_len] in temp and temp[s[j:j+word_len]]==word_counts[s[j:j+word_len]]:
                    break
                else:
                    temp[s[j:j + word_len]] = temp.get(s[j:j + word_len], 0) + 1
                    j += word_len
            # print(temp)
            if temp == word_counts:
                # print(i)
                res.append(i)
    return res


res = string_decomposition("amanaplanacanaplal",["can","ana","apl"])
print(res)


##Time complexity : Each index(in N indices), at worse we travese through all words of size n and length m

## O(Nnm).

## Note that list/string slice has time complexity of slice size. For examples l = [1,2,3,4,5] or s = "abcde"

## since form indices 2-4, noting but looping from indices 2to4 has time compleixy O(2). More generally O(slice size).