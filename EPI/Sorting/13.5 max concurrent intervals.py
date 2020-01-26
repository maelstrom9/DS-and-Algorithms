

## doing a variant of max intervals

## max bandwidth.

def max_bandwidth(arr):

    # form all endpoints with start or end notations and bandwidths.

    endpoints = [(event[0],True,event[2]) for event in arr] + [(event[1],False,event[2]) for event in arr]

    endpoints.sort()

    m_b = float("-inf")
    l_b = 0
    for e in endpoints:
        if e[1]:
            l_b += e[2]
        else:
            l_b -= e[2]
        m_b = max(m_b,l_b)
    return m_b

res = max_bandwidth([(1,10,2),(1,5,6),(2,11,12),(5,8,0),(5,9,20),(6,16,15)])
print(res)
