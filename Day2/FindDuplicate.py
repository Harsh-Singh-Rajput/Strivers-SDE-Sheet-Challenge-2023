def findDuplicate(arr:list, n:int):
    l = [0] * n
    for val in arr:
        if l[val - 1] == 1:
            return val
        else:
            l[val - 1] += 1
    