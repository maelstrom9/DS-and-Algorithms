


## arr represents daily stock prices..

## return the max profilt


def buy_sell_once(arr):
    m_p = 0
    prev = 0
    res = []
    for i in range(1,len(arr)):
        curr = max(prev+arr[i]-arr[i-1],arr[i]-arr[i-1])
        prev = curr
        m_p = max(curr,m_p)
        res.append(curr) ## res.append(max(0,curr)) will also work....
    return [0]+res


def buy_sell_twice(arr):
    x = buy_sell_once(arr)
    y = buy_sell_once([-i for i in reversed(arr)])
    print(x,y)
    res = [x[i]+y[i+1] if i<len(arr)-1 else x[i] for i in range(len(arr))]
    return max(res)

print(buy_sell_twice([12,11,13,9,12,8,14,13,15]))


## solution from the book

def buy_sell_once_book(arr):
    min_so_far = float("inf")
    max_profit = 0
    for i in range(len(arr)):
        min_so_far = min(min_so_far,arr[i])
        max_profit = max(max_profit,arr[i]-min_so_far)
    return max_profit

def buy_sell_twice_book(arr):
    min_so_far = float("inf")
    max_profit = 0
    first_buy = []
    for i in range(len(arr)):
        min_so_far = min(min_so_far, arr[i])
        max_profit = max(max_profit, arr[i] - min_so_far)
        first_buy.append(max_profit)
    max_so_far = float('-inf')
    max_profit = 0
    for j in range(len(arr)-1,0,-1):
        max_so_far = max(max_so_far,arr[j])
        max_profit = max(max_so_far-arr[j]+first_buy[j-1],max_profit)
    return max_profit

print(buy_sell_twice_book([12,11,13,9,12,8,14,13,15]))