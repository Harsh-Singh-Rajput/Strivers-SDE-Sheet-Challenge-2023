def maximumProfit(prices):
    ans = 0
    localmin = prices[0]
    localmax = 0
    for i in range(1,len(prices)):
        ans = max(ans, prices[i] - localmin)
        if localmin > prices[i]:
            localmin = prices[i]
    return ans