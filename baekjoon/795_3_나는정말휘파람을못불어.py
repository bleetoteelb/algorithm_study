N = int(input())
S = input()

Ecnt = [ 0 for _ in range(N+1) ]
ws = 0
Hs = []

for i in range(N):
    if S[N-1-i]=='E':
        Ecnt[N-1-i] = Ecnt[N-i]+1
    else:
        Ecnt[N-1-i] = Ecnt[N-i]
for i in range(N):
    if S[i]=="W":
        ws += 1
    elif S[i]=="H":
        Hs.append([i,ws])


print(Ecnt)
print(Hs)
answer = 0
for h in Hs:
    es = Ecnt[h[0]]
    print(h,es)
    answer += h[1] * (es * (es-1) //2)
print(answer)
        

    
