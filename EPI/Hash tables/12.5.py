



def find_nearest_repeated_entries(arr):

    dict = {}

    dist = float("inf")

    for idx in range(len(arr)): ## enumerate is better usage.. obviously
        if arr[idx] in dict:
            d = idx - dict[arr[idx]]
            dist = min(dist,d)

        dict[arr[idx]] = idx

    # return dist .. what if it remains float(inf)
    return dist if dist!=float('inf') else -1

res = find_nearest_repeated_entries(["All","work","and","no","play","makes","for","no","work","no","fun","and","no","results"])

print(res)