def nextPermutation(permutation, n):
    
    ind = -1
    for i in range(n-2, -1, -1):
        if permutation[i] < permutation[i + 1]:

            ind = i
            break

    if ind == -1:

        permutation.reverse()
        return permutation

    for i in range(n - 1, ind, -1):
        if permutation[i] > permutation[ind]:
            permutation[i], permutation[ind] = permutation[ind], permutation[i]
            break

    permutation[ind+1:] = reversed(permutation[ind+1:])

    return permutation