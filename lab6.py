import time

def recursive_binary_search(arr, low, high, target):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursive_binary_search(arr, mid + 1, high, target)
    else:
        return recursive_binary_search(arr, low, mid - 1, target)

# Generate sorted list of at least 100,000 integers
data = list(range(1, 100001))
target_value = 87654

# Measure execution time
start_time = time.perf_counter()
result = recursive_binary_search(data, 0, len(data) - 1, target_value)
end_time = time.perf_counter()
execution_time = end_time - start_time

print("--- RECURSIVE BINARY SEARCH ---")
print(f"Target Found at Index: {result}")
print(f"Time Taken: {execution_time:.7f} seconds")