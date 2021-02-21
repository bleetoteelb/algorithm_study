def solution(progresses, speeds):
    day = 0
    cnt = 0
    i = 0
    size = len(progresses)
    answer = []
    while (i < size):
        if (progresses[i]+speeds[i]*day >= 100):
            cnt += 1
            i += 1
        else:
            if (cnt > 0):
                answer.append(cnt)
                cnt = 0
            day += 1
                
    answer.append(cnt)
        
    return answer
