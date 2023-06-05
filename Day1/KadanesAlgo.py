def maxSubarraySum(arr, n):
    ans = 0
    curr = 0

    for val in arr:
        if curr > 0:
            curr += val
        else:
            curr = val
        ans = max(curr, ans)

    return ans