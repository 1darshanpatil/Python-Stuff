N = int(input())
p = [[0]*(N+1) for i in range(N+1)]
for i in range(N+1):
    p[i][1] = 1
    p[i][i] = 1
for n in range(2, N+1):
    for k in range(2, n+1):
        p[n][k] = p[n-1][k-1] + p[n-k][k]
#print(p[-1]) 
#print(sum(p[-1]))
#print(len(str(sum(p[-1]))))
import matplotlib.pyplot as plt
x = list(range(1, N+1))
y = p[N][1:]
#print(x);print(y)
plt.plot(x, y)
plt.show()
print(max(p[N][1:]))
'''
for ind, x in enumerate(p):
    mx = max(x)
    s = x[1:ind]
    print(s)
    #print('#' + str(ind), sum(x), x.index(mx), 'cbrt' + str(ind**(1/2)))
'''
