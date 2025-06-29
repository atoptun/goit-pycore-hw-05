from typing import Callable

def caching_fibonacci() -> Callable[[int], int]:
    """Returns a cached Fibonacci function"""
    cache = {1: 1}
    def fibonacci(num: int) -> int:
        """Returns a Fibonacci number"""
        if num in cache:
            return cache[num]
        if num <= 0:
            return 0
        cache[num] = fibonacci(num - 1) + fibonacci(num - 2)
        return cache[num]
    
    return fibonacci


fibonacci = caching_fibonacci()
print(fibonacci(7))
print(fibonacci(20))
print(fibonacci(10))
