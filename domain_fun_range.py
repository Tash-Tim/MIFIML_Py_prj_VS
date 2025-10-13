from sympy import Symbol, S
from sympy.calculus.util import continuous_domain, function_range
x = Symbol("x") 
f = (x**3)/(x**2-1) 
print(continuous_domain(f, x, S.Reals))
print(function_range(f, x, S.Reals))