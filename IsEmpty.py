from ArrayStack import ArrayStack
import time

stack = ArrayStack()

for n in [100000, 500000, 1000000]:

    start = time.perf_counter()

    for i in range(n):
        stack.is_empty()

    end = time.perf_counter()

    print("Number of Calls:", n)
    print("Is_empty Time:", end - start, "seconds")
    print()