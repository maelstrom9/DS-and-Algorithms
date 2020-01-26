


def kth_element_spiral(arr,k):
    ## should be 2d..meaning both m and n.. >1
    m,n = len(arr),len(arr[0])
    ## k should be in appropriate range
    if k>m*n:
        return -1
    s = 2*(m-1)+2*(n-1)

    k_ = k
    ## to avoid this loop solve the equality of arithemetic sum... ref: https://en.wikipedia.org/wiki/Arithmetic_progression#Sum
    ## ref2 : https://gist.github.com/lopespm/a5e6552451227f1ea04579e7ec750c4d
    while s<k:
        k_ -= 2 * (m - 1) + 2 * (n - 1)
        m-=2
        n-=2
        s+=2*(m-1)+2*(n-1)


    k=k_

    ### 0--> row is 0, for col add remainder to 0
    ### 1--> col is n-1, for row add remainder to 0
    ### 2--> row is m-1, for col sub remainder from n-1
    ### 3--> col is 0, for row sub remainder from m-1

    if m==1:
        row = m-1
        col = k-1 ## rem
    elif n==1:
        row = k-1 ## rem
        col = n-1
    else:

        bi_index, rem = divmod(k-1,n-1+m-1)

        if bi_index==0:
            idx,rem = divmod(k-1,m-1)
            if idx==0:
                quad_idx = idx
                rem = rem
            else:
                quad_idx = 1
                _,rem = divmod(k-1-m+1,n-1)
        else:
            idx, rem = divmod(k-1-m+1-n+1, m - 1)
            if idx == 0:
                quad_idx = 2
                rem = rem
            else:
                quad_idx = 3
                _, rem = divmod(k - 1 - 2*m + 2-n+1, n - 1)

        if quad_idx==0:
            row = 0
            col = rem
        elif quad_idx==1:
            row = rem
            col = n-1
        elif quad_idx==2:
            row = m-1
            col = n-1-rem
        else:
            row = m-1-rem
            col = 0

    return arr[row+(len(arr)-m)//2][col+(len(arr[0])-n)//2]


arr = [[1,2,3,4],[4,3,5,8],[9,12,11,21],[1,1,1,1]]
print(kth_element_spiral(arr,16))