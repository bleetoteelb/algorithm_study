N = int(input())

z = []
while(N>0):
    z.append(N%2)
    N = N//2
answer = []
for i in range(len(z)):
    answer.append(str(z[-1-i]*2))
print(''.join(answer))
