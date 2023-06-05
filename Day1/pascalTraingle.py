
def printPascal(n: int):
    ans = []

    def getValue(n, r):
        res = 1
        for i in range(r):
            res = res * (n - i)
            res = res // (i + 1)
        return int(res)
    for row in range(1, n+1):
        tempLst = [] # temporary list
        for col in range(1, row+1):
            tempLst.append(getValue(row - 1, col - 1))
        ans.append(tempLst)
    return ans


