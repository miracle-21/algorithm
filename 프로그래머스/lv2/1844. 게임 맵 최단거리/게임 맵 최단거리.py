from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    q = deque([(0,0)])
    while q:
        x,y = q.popleft()
        for i in range(len(directions)):
            nx = x + directions[i][0]
            my = y + directions[i][1]
            if 0 <= nx < n and 0 <= my < m and maps[nx][my] == 1:
                maps[nx][my] = maps[x][y]+1
                q.append((nx,my))
    return maps[-1][-1] if maps[-1][-1] > 1 else -1