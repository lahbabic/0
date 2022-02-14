import math
import time

number = []
number1 = []
for i in range(1, 100):
    number.append(math.exp(i)+math.log(i, 2))
for i in range(1, 100):
    number1.append(math.exp(i)-math.log(i, 2))

a = (number[98] - number[0])/99
print(a)
print(number[0])
a = (number1[98] - number1[0])/99
print(a)
print(number1[0])








