from datetime import datetime
import time

def solution(lines):
    answer = 0
    lines2 = []
    lines3 = []
    idx = 0
    for line in lines:
        blank = line.split(' ')
        tmp = ' '.join([blank[0],blank[1].split('.')[0]])

        tt = time.mktime(datetime.strptime(tmp,'%Y-%m-%d %H:%M:%S').timetuple())
        tt = int(tt)*1000+int(blank[1].split('.')[1])

        last = int(float((blank[2].split('s'))[0])*1000)
        # (시작시간, 마치는 시간)
        lines2.append((tt-last+1,tt))
        # (시작시간 or 마치는 시간)
        lines3.append(tt-last+1)
        lines3.append(tt)
        idx= idx+1

    sorted_line = sorted(lines2, key=lambda lines2:lines[0])
    sorted_all = sorted(lines3)

    print(lines2)
    print(lines3)
    idx = 0
    for ln in sorted_all:
        num = 0
        for a,b in sorted_line:
            if ln >= a and ln <= b:
                num = num+1
                print("1")
            elif ln <= a and ln+1000 >= b:
                num = num+1
                print("2")
            elif ln+1000 >= a and ln+1000 <= b:
                num = num+1
                print("3")
            elif ln+1000 <= a:
                break
        if(answer<num):
            answer = num
    return answer
