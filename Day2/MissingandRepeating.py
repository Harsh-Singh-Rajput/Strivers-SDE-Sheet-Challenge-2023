from collections import Counter

def missingAndRepeating(arr, n):
    dic = Counter(arr)
    repeating = None
    missing = None
    for i in range(1, n + 1):
        if i not in dic:
            missing = i
        if dic[i] == 2:
            repeating = i
    return (missing, repeating)
