x = int(input("Enter Int > 2: "))
primes_using_all = list(filter(lambda N: all(list(N%n for n in range(2, x))), range(2, 100)))
primes_using_double_loop = list(N for N in range(2, x) if all(N%n for n in range(2, N)))

import sympy
primes_using_sympy = list(N for N in range(2, x) if sympy.isprime(N))
print(primes_using_all); print(primes_using_doubl_loop); print(primes_using_sympy)
