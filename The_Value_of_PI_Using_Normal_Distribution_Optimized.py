import random
from math import e, pi
N = int(input("Enter the value of N: "))
M = int(input("Enter the value of M: "))
N0 = 0.0     #Convert to float for speed improvement
half_M = M//2
#t1 = time.time()
for _ in range(N):
    if random.choices((True, False), k = M).count(True) == half_M:
        N0 = N0 + 1        #Variable += delta takes longer time


#print(f"Time of execution: {time.time() - t1}")
print(f"N = {N}\nM = {M}\nN0 = {N0}")
pi_ = (2/M)*(N/N0)**2*e**(-1/(2*M))
print(f"The pi_ = {pi_}"); print(f"Error %: {round((pi_ - pi)*100)}")
