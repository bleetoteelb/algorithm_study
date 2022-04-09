import heapq as h

N, K = map(int,input().split(' '))
ps = list(map(int,input().split(' ')))
large = ps[:K]
h.heapify(large)

center = large[0]
h.heappop(large)

# first line K
print(center)
for i in range(K,N):
    if ps[i] > center:
        h.heappush(large,ps[i])
        center = large[0]
        h.heappop(large)
    print(center)

