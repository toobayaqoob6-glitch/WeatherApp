from ArrayStack import ArrayStack
import time

for n in [100000, 500000, 1000000]:
    stack = ArrayStack()

    # Stack mein elements add karna
    for i in range(100):
        stack.push(i)

    start = time.perf_counter()

    # Top operation repeatedly perform karna
    for i in range(n):
        stack.top()

    end = time.perf_counter()

    print("Number of Top Calls:", n)
    print("Top Time:", end - start, "seconds")
    print()