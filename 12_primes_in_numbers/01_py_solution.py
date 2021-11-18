import time
def prime_factors(n):
    result = n * 1
    count = 0
    primes_str = ''
    for i in [*range(2, 3), *range(3, 2 + int(n**0.5), 2)]:
        while (result % i == 0):
            count += 1
            result /= i
            if result % i != 0:
                primes_str += f'({i})' if count == 1 else f'({i}**{count})'
                count = 0
            
    return primes_str if result < 2 else primes_str + f"({int(result)})" 

t0 = time.time()
# print(prime_factors(100))
print(prime_factors(77587891222))
t1 = time.time()
print("Time required :", (t1 - t0)*1000)