# Exercise: genPrimes
# 5/5 points (graded)
# ESTIMATED TIME TO COMPLETE: 10 minutes

# Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...

def genPrimes():
    primes = []
    n = 2
    last = n

    while True:
        for i in primes:
            if n % i == 0:
                n += 1
                break

        else:
            primes.append(n)
            last = n
            n += 1
            yield last
