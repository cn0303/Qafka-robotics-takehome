#!/usr/bin/env python3
import numpy as np
n, m = map(int, input().split())
A = np.zeros((n, n), dtype=int)
for i in range(m):
    x, y, r = map(int, input().split())
    for dx in range(-r, r + 1):
        for dy in range(-r, r + 1):
            if abs(dx) + abs(dy) <= r:
                nx, ny = x - 1 + dx, y - 1 + dy
                if 0 <= nx < n and 0 <= ny < n:
                    A[nx][ny] += 1
print(np.amax(A))