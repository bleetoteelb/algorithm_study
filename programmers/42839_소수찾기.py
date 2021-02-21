from itertools import permutations

def solution(numbers):
    candi = set()
    for i in range(1,len(numbers)+1):
        candi |= set(map(lambda x:int(''.join(x)),list(permutations(numbers,i))))
    candi -= set(range(0,2))

    for i in range(2, int(max(candi) ** 0.5) +1):
        candi -= set(range(i*2, max(candi)+1, i))

    return len(candi)



samples = ["17","011"]

for i in samples:
    print(solution(i))
