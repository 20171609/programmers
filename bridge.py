from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)],maxlen = bridge_length)
    truck_sum = 0

    while truck:
        truck_sum -= bridge[0]
        
        answer += 1
        
        if truck_sum + truck[0] <= weight:
            truck_sum += truck[0]
            bridge.append(truck.popleft())
        
        else:
            bridge.append(0)
            
    answer += bridge_length
    
    return answer
