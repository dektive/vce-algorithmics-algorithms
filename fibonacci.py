def fibonacci_topdown(n, memory=None):
    print(memory, n)
    if memory is None:
        memory = {0: 0, 1: 1}
    if n in memory:
        return memory[n]
    else:
        memory[n] = fibonacci_topdown(n - 1, memory) + fibonacci_topdown(n - 2, memory)
        return memory[n]


def fibonacci_bottomup(n):
    memory = {0: 0, 1: 1}
    for i in range(2, n+1):
        memory[i] = memory[i - 1] + memory[i - 2]

    return memory[n]

#print(fibonacci_bottomup(12))
print(fibonacci_topdown(5))
