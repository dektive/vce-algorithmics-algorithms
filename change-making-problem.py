def coin_change(sum, coins):
    DP = [float("infinity")]*(sum+1)
    DP[0] = 0
    for i in range(1, sum+1):
        for coin in coins:
            if i - coin >= 0:
                print(i, DP)
                DP[i] = min(DP[i], DP[i-coin] + 1)
    return DP[-1] if DP[-1] < float('infinity') else False


