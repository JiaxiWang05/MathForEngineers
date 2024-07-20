import math
from sympy import isprime, primefactors, totient

def count_factors_in_factorial(n, p):
    """ Count the number of factors of prime p in n! """
    count = 0
    power = p
    while power <= n:
        count += n // power
        power *= p
    return count

def multiplicative_order(q, p, a):
    """ Find the smallest d such that q^d ≡ 1 (mod p^a) """
    order = 1
    current = q % (p ** a)
    while current != 1:
        current = (current * q) % (p ** a)
        order += 1
    return order

def is_integer(n, q):
    """ Check if X = (1 / (n! * (q-1)^n)) * ∏(q^i - 1) is an integer """
    product = 1
    for i in range(1, n + 1):
        product *= (q ** i - 1)

    # Check for prime factors
    for p in primefactors(math.factorial(n)):
        count_in_factorial = count_factors_in_factorial(n, p)
        b = 0
        while (q - 1) % p == 0:
            q_minus_1 = q - 1
            while q_minus_1 % p == 0:
                q_minus_1 //= p
                b += 1

        sufficient_factors = True
        for a in range(1, count_in_factorial + 1):
            d_a = multiplicative_order(q, p, a + b)
            if d_a > p ** a:
                sufficient_factors = False
                break

        if not sufficient_factors:
            return False

    return True

def is_relatively_prime_to_half_q_minus_1(n, q):
    """ Check if X is relatively prime to (q-1)/2 """
    half_q_minus_1 = (q - 1) // 2
    x_value = 1 / (math.factorial(n) * (q - 1) ** n)
    for i in range(1, n + 1):
        x_value *= (q ** i - 1)

    for p in primefactors(half_q_minus_1):
        if x_value % p == 0:
            return False

    return True

 
