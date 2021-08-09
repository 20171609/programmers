def solve(array, a):
    
    if  a[0] == a[1]:
        array = [array[a[0]-1]]
    elif a[1] < len(array):
        array = array[a[0]-1:a[1]]
    else:
        array = array[a[0]-1:]
    
    array.sort()
    return array[a[2]-1]
    
    

def solution(array, commands):
    answer = []
    
    for i in commands:
        answer.append(solve(array, i))
    
    
    return answer
