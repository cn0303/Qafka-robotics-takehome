#!/usr/bin/env python3
import math
def euc_dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)

def bfs(stations, max_dist):
    n = len(stations)
    visited = [False] * n
    queue = [0]  
    visited[0] = True
    while queue:
        current = queue.pop(0)
        if current == n - 1: 
            return True
        for i in range(n):
            if not visited[i] and euc_dist(stations[current], stations[i]) <= max_dist:
                visited[i] = True
                queue.append(i)
    return False

def binary_search(stations):
    low, high = 0, euc_dist(stations[0],stations[-1])  
    dist = high
    while high - low >= 0.001: 
        mid = (low + high) / 2
        if bfs(stations, mid):
            dist = mid
            high = mid
        else:
            low = mid
    return dist

def main():
    zearth = tuple(map(float, input().split()))
    n = int(input())
    stations = [(0.0, 0.0, 0.0)] 
    for i in range(n):
        stations.append(tuple(map(float, input().split())))
    stations.append(zearth) 
    max_dist = binary_search(stations)
    print(f"{max_dist:.2f}")

if __name__ == "__main__":
    main()