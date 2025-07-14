import random
from sympy import Symbol, interpolate

def create_shares(secret, n, t):
    coeffs = [secret] + [random.randint(1, 100) for _ in range(t-1)]
    shares = [(i, sum([coeffs[j] * (i ** j) for j in range(t)])) for i in range(1, n+1)]
    return shares

def reconstruct_secret(shares):
    x = Symbol('x')
    points = [(share[0], share[1]) for share in shares]
    polynomial = interpolate(points, x)
    return int(polynomial.subs(x, 0))