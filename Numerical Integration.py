""" TRAPEZOIDAL RULE """

"""Initializing Variables"""

a = 0     # lower limit
b = 1     # upper limit
n = 100   # no of division in the graph

sum1 = 0      # for sum from y(0) to y(n)
sum2 = 0      # for sum from y(1) to y(n-1)

"""Formulas """

h = (b - a) / n         # concept discussed in the pdf file (attached in the same repo)
multiplier = b / n      # to be multiplied with x everytime (concept in the theory)


def integration(x):                                    # defined a function which takes input x and returns the integration answer
    integ_x = 1 / (1 + (x * multiplier) ** 2)          # one of the integration example
    return integ_x

""" SUM 1 """                                          # for sum from y(0) to y(n)

for i in range(0, n + 1):
    print("iter" + str(i) + ',', "x =", i * multiplier)
    print("y =", integration(i))
    sum1 = sum1 + integration(i)

print("---------------------------------")                   # a simple dash line to separate sum1 and sum2

""" SUM 2 """                                          # for sum from y(1) to y(n-1)

for i in range(1, n):
    print("iter" + str(i) + ',', "x =", i * multiplier)
    print("y =", integration(i))
    sum2 = sum2 + integration(i)


integ = (h / 2) * (sum1 + sum2)                             # applying final formula to calculate integration
print("Final Integration Answer:", integ)

""" TRY IT FOR YOURSELF (remember to multiply only the 'x' term with the multiplier) 

1. I1 = 1 / (1 + x**2)       
2. I2 = 2.71**(x**2)         # e^x^2

"""