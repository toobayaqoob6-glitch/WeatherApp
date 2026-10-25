from ArrayStack import ArrayStack
import time

for n in [10000, 100000, 500000, 1000000]:
    stack = ArrayStack()

    # Stack ko elements se fill karna
    for i in range(n):
        stack.push(i)

    start = time.perf_counter()

    # Saare elements pop karna
    for i in range(n):
        stack.pop()

    end = time.perf_counter()

    print("Number of elements:", n)
    print("Pop Time:", end - start, "seconds")
    print()