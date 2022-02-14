import math
import time

number = []
number1 = []
for i in range(1, 100):
    number.append(math.exp(i)+math.log(i, 2))
    number1.append(math.exp(i)-math.log(i, 2))
a = (number[50] - number[0])/50
a = (number1[50] - number1[0])/50
print(a)
print(number[0])
print(a)
print(number1[0])
