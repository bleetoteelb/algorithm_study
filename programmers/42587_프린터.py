import queue
def solution(priorities, location):
    answer = 1
    qp = queue.Queue()
    qp_s = queue.PriorityQueue()
    times = 0
    for i in priorities:
        qp.put(i)
        qp_s.put(i*(-1))
        
    while(True):
        item = qp.get()
        high = qp_s.get()
        if (high*(-1) > item):
            qp.put(item)
            qp_s.put(high)
            if (location == 0):
                location = qp.qsize()-1
            else:
                location -= 1
        else:
            if (location == 0):
                break;
            else:
                location -= 1
                answer += 1
    
    return answer
