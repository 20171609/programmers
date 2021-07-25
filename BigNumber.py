def solution(numbers):
    answer = ''
    
    str_list = []
    
    for i in numbers:
        str_list.append(str(i))
    
    str_list.sort(key = lambda x : (x[0], x * 3), reverse = True)
    
    for i in str_list:
        answer += i
    
    if set(answer) == {'0'}:
        return "0"
    
    return answer