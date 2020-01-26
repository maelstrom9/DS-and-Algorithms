



def longest_sub_array_dist_entries(arr):

    if not arr:
        return -1

    dict = {}
    start = 0
    g_dist = (0,0)
    for end,word in enumerate(arr):
        if word in dict and start<=dict[word]: ### start cant be crossing the word..
            start = dict[word] + 1

        dict[word] = end
        if end-start>g_dist[1]-g_dist[0]: g_dist = (start,end)
    return arr[g_dist[0]:g_dist[1]+1]

print(longest_sub_array_dist_entries(list("wkwkrsommgirss")))