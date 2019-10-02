# For loops over a given sequence.

primes = [2, 3, 5, 7]
for prime in primes:
    print(prime, end=' ')
    pass

# For loops can iterate over a sequence of numbers using `range` and `xrange`.
# Python 3 uses the `range` function, which acts like `xrange`.
print()
for x in range(5):
    print(x, end=' ')
    pass

print()
for x in range(3,8):
    print(x, end=' ')
    pass

print()
for x in range(3,8,2):
    print(x, end=' ')
    pass