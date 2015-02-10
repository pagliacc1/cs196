from math import sqrt

primes = [2]

def is_prime(n):
    for i in primes:
        if n % i == 0:
            output = False
            break
        elif i > sqrt(n):
            output = True
            break
    return output
        
def generate_primes(n):
    c = 3
    while len(primes) < n:
        if is_prime(c) == True:
            primes.append(c)    
        c += 2
                
generate_primes(10001)
print(primes[-1:])