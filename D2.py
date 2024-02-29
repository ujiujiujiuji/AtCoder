import math
import sympy
x = sympy.Symbol('x')
N, M, K = list(map(int,input().split()))
g = math.lcm(N,M)
#x = K*N*M*g/(M*g+N*g-2*M*N)
equation = x//M + x//N - 2*(x//g) - K
print(sympy.solve(equation))
