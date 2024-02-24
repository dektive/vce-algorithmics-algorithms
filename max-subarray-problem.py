def max_subarray_sum(P):
    n = len(P)
    best = [0] * n
    best[0] = P[0]

    for i in range(1, n):
        print(P[i], best[i-1])
        best[i] = max(P[i], P[i] + best[i - 1])

    return max(best)

print(max_subarray_sum([20, -40, 90, 20, -50, 70]))