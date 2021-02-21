def solution(n):
    answer = []
    while(n > 0):
        print(n)
        a = n%3
        if a == 1: answer.append(1)
        elif a == 2: answer.append(2)
        else:
            answer.append(4)
            a = 3
        n = (n - a)//3
         
    return ''.join(map(str,reversed(answer)))
