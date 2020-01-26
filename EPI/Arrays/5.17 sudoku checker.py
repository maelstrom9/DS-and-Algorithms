
## duplicate finding in array based solution..
## this is not valid as the same spots are used for checking different valuess..
def sudoku_checker(arr):

    m,n = len(arr),len(arr[0])

    for row in range(m):
        for col in range(n):
            val = abs(arr[row][col])
            index = 9-val
            if val!=0.5:
                if arr[row][index] < 0:
                    return False
                arr[row][index] = -arr[row][index]
                if arr[index][col] < 0:
                    return False
                arr[index][col] = -arr[index][col]
                ri, ci = row-row%3,col-col%3
                ri, ci = ri+index%3,ci+index%3
                if arr[ri][ci] < 0:
                    return False
                arr[ri][ci] = -arr[ri][ci]
    return True


arr= [[0.5]*9 for i in range(9)]
arr[0][0] = 5
arr[6][6] = 5

print(sudoku_checker(arr))