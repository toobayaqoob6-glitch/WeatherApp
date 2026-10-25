from ArrayStack import ArrayStack
import time

for n in [10000, 100000, 500000, 1000000]:
    stack = ArrayStack()

    start = time.perf_counter()

    for i in range(n):
        stack.push(i)

    end = time.perf_counter()

    print("Number of elements:", n)
    print("Push Time:", end - start, "seconds")
    print()