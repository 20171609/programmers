def solution(progresses, speeds):
    answer = []
    
    rest_task = []
    
    for i in range(len(progresses)):
        num = 100-progresses[i]
        
        if num % speeds[i]:
            rest_task.append((num // speeds[i]) + 1)
        
        else:
            rest_task.append(num // speeds[i])
    
    tmp = rest_task[0]
    count = 1
    
    for i in range(1, len(rest_task)):
        if tmp >= rest_task[i]:
            count += 1
    
        
        else:
            answer.append(count)
            tmp = rest_task[i]
            
            count = 1
    
    answer.append(count)
        
    
    return answer