import math
import time
exp = []
log = []
for i in range(1, 100):
    exp.append(math.exp(i)+math.log(i, 2))
    log.append(math.exp(i)-math.log(i, 2))
a = (exp[50] - exp[0])/50
a = (log[50] - log[0])/50
print(a)
print(exp[0])
print(a)
print(log[0])
