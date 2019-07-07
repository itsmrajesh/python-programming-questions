from functools import lru_cache
import time


@lru_cache()
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)


t0 = time.time()
for i in range(1, 28):
    t1 = time.time()
    print(fibonacci(i))

print(f"Total time is :-{t1-t0}")
