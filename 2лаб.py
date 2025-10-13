
#1 задача

def f(x):
    if -2 <= x or x < 2:
        return x**2
    elif x >= 2:
        return x**2 + 4*x + 5
    else x < -2:
        return 4
    
#2 задача

import math

return math.gcd(a,b)

#3 задача
нет решения


#4задача
def sum_of_digits(number):
    return sum(int(digit) for digit in str(abs(number)))

    