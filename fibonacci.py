import time
from functools import lru_cache
import sys

sys.setrecursionlimit(2000)

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def print_fibonacci(n):
    start = time.perf_counter()
    print([fibonacci(i) for i in range(n)])
    print(f"Runtime: {time.perf_counter() - start:.6f} seconds")

print_fibonacci(1000)
