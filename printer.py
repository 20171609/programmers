from collections import deque

def solution(priorities, location):
    answer = 0
    que = deque([i for i in priorities])
    
    maxnum = max(que)

    while (que):
        if que[0] == maxnum:
            que.popleft()
            answer += 1
            if location == 0:
                break
            
            maxnum = max(que)
            location -= 1
        
        else:
            print(que[0])
            if location == 0:
                location = len(que)
            location -= 1
            que.append(que.popleft())
        
    return answer
