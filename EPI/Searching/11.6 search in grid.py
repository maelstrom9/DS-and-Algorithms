



## OPTIMAL solution

def g_search(M,k):

    if not M or not M[0]:
        return False

    r,c = 0,len(M[0])-1

    while r<len(M) and c>=0:
        if M[r][c]==k:
            return True
        elif M[r][c]>k:
            c-=1
        else:
            r+=1
    return False

M = [[-1,2,4,4,6],[1,5,5,9,21],[3,6,6,9,22],[3,6,8,10,24],[6,8,9,12,25],[8,10,12,13,40]]

print(g_search(M,22))

## Time complexity O(m+n-1)



## SUB_OPTIMAL mlog(n) or nlog(m)
def col_search(M,r,s,e,k):
    while s<=e:
        m = s + (e-s)//2
        if M[r][m]==k:
            return m
        elif M[r][m]>k:
            e = m-1
        else:
            s = m+1
    return -1

def row_search(M,c,s,e,k):
    while s<=e:
        m = s + (e-s)//2
        if M[m][c]==k:
            return m
        elif M[m][c]>k:
            e = m-1
        else:
            s = m+1
    return -1



def search_grid(M,k):

    if not M or not M[0]:
        return False

    r, c  = len(M), len(M[0])

    if r>=c:
        for i in range(r):
            if M[i][c-1]>=k:
                if col_search(M,i,0,c-1,k)>=0:
                    return True
    else:
        for i in range(c):
            if row_search(M,i,0,r-1,k)>=0:
                return True

    return False

# M = [[-1,2,4,4,6],[1,5,5,9,21],[3,6,6,9,22],[3,6,8,10,24],[6,8,9,12,25],[8,10,12,13,40]]

# print(search_grid(M,8))




