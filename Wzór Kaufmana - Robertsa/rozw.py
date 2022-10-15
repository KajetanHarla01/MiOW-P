M = int(input("Podaj liczbę strumieni: "))
t = []
a = []
x = []
P = []

for i in range(0, M):
    ti = int(input("Podaj t" + str(i+1) + ": "))
    t.append(ti)
    
for i in range(0, M):
    ai = int(input("Podaj a" + str(i+1) + ": "))
    a.append(ai)
    
V = int(input("Podaj pojemnosc systemu: "))

x.append(float(1))

for n in range(1, V):
    sum = float(0)
    for i in range(0, M):
        if t[i] < n:
            sum += t[i] * a[i] * x[n - t[i]]
        elif t[i] == n:
            sum += t[i] * a[i]
    x.append(sum/n)

sum = 0
for n in range(0, V):
    sum += x[n]

P.append(1 / sum)

for n in range(1, V):
    P.append(x[n] * P[0])
    
print("Prawdopodobienstwa stanu zajetosci kanalow:")

for n in range(0, len(P)):
    print("P(" + str(n) + ") = " + str(round(P[n], 4)))
    
i = int(input("Podaj klase i: "))

b = 0

for n in range(V - t[i-1] + 1, V):
    b += P[n]

print("b(" + str(i) + ") = " + str(round(b, 4)))
