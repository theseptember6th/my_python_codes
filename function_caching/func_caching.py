import time
from functools import lru_cache

# Applying lru_cache decorator to cache the results of func1
@lru_cache(maxsize=3)
def func1(n):
    time.sleep(n)  # Simulate a time-consuming function
    return f"executed successfully"

if __name__ == '__main__':
    print("for func1(3)")
    print(func1(3)) # takes 3 seconds and is now saved in cache
    print(func1(3)) # returns instantly
print(func1(3)) # returns instantly
print(func1(3)) # returns instantly

print("for func1(5)")
print(func1(5)) # takes 5 seconds and is now saved in cache
print(func1(5)) # returns instantly
print(func1(5)) # returns instantly
print(func1(5)) # returns instantly
print(func1(5)) # returns instantly

print("for func1(8)")
print(func1(8)) # takes 8 seconds and is now saved in cache
print(func1(8)) # returns instantly
print(func1(8)) # returns instantly
print(func1(8)) # returns instantly

print("for func1(2)")
print(func1(2)) # takes 2 seconds and is now saved in cache (oldest cache entry will be removed)
print(func1(2)) # returns instantly
print(func1(2)) # returns instantly
print(func1(2)) # returns instantly

print("for func1(4)")
print(func1(4)) # takes 4 seconds and is now saved in cache (oldest cache entry will be removed)
print(func1(4)) # returns instantly
print(func1(4)) # returns instantly
print(func1(4)) # returns instantly

# Test older cache eviction
print("Testing cache eviction")
print(func1(3)) # takes 3 seconds again as it was evicted from the cache
print(func1(5)) # returns instantly as it is still in the cache
print(func1(8)) # returns instantly as it is still in the cache

# Current cache: func1(2), func1(4), func1(3)

print(func1(2)) # returns instantly
print(func1(4)) # returns instantly
print(func1(3)) # returns instantly

print(func1(5)) # takes 5 seconds again as it was evicted from the cache
print(func1(8)) # takes 8 seconds again as it was evicted from the cache
