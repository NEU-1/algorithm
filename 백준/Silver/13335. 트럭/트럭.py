from collections import deque

N, M, T = map(int,input().split())

trucks = deque(map(int,input().split()))
time = 0
bridge = deque([0]*M)
weight = 0

while trucks or weight > 0:
    time += 1

    pop_truck = bridge.popleft()
    if pop_truck > 0:
        weight -= pop_truck
    
    if trucks and weight + trucks[0] <= T:
        truck = trucks.popleft()
        bridge.append(truck)
        weight += truck
    else:
        bridge.append(0)
print(time)

