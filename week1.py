# https://www.acmicpc.net/problem/17143


# 1초당 움직이는것을 for문의 i가 1씩 증가할때마다로 구현

# 1. 낚시꾼 0,0에서 0,+1 이동
# 2. 해당 열의 상어중 가장 가까운 상어를 잡는다
# 3. 잡으면 상어는 없어진다
# 4. 상어가 보고있는 방향으로 주어진 속도 만큼 이동한다
# 5. 상어는 같은칸에 있을시 크기가 가장 큰 상어가 나머지를 모두 먹는다

# 결과 : 잡은 상어 크기의 합을 구하라

# 상어 이동 함수
def move_shark():
    g = [[[] for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if graph[i][j]:
                x, y = i, j
                s, d, z = graph[i][j][0]
                dist = s
                # 상어의 속도만큼 1칸씩 이동
                while 0 < dist:
                    nx = x + shark_direction[d][0]
                    ny = y + shark_direction[d][1]
                    # 맵 내부에서 이동하는 경우
                    if 0 <= nx < R and 0 <= ny < C:
                        x, y = nx, ny
                        dist -= 1 # 이동해야 할 남은 거리 1 차감
                    # 벽과 충돌하는 경우, 현재 진행방향별 방향전환
                    else:
                        # d(0-1-2-3) : 방향(상-하-우-좌)
                        # 상 to 하 or 우 to 좌
                        if d == 0 or d == 2:
                            d += 1
                        # 하 to 상 or 좌 to 우
                        elif d == 1 or d == 3:
                            d -= 1
                        continue
                g[x][y].append([s, d, z])

    for i in range(R):
        for j in range(C):
            graph[i][j] = g[i][j]

def eat_shark():
    for m in range(R):
        for n in range(C):
            # 한 좌표에 상어가 2마리 이상 있는 경우
            if 1 < len(graph[m][n]):
                # 몸집이 작은 순서대로 상어 제거
                graph[m][n].sort(key=lambda x: x[2], reverse=True)
                while 1 < len(graph[m][n]):
                    graph[m][n].pop()

# 상어 낚시 함수
def catch_shark():
    global answer
    # 낚시왕이 칼럼 방향으로 이동하며 낚시를 하기 때문에 칼럼 우선순위
    for i in range(C):
        for j in range(R):
            # 상어가 존재하는 경우
            if graph[j][i]:
                answer += graph[j][i][0][2]
                graph[j][i].remove(graph[j][i][0])
                break
        move_shark()
        eat_shark()


if __name__ == '__main__':
    # 격자판 RxC
    R, C, M = map(int, input().split())
    # 상어의 위치 cr, s속력, d이동방향 이동방향은(1:위 2:아래 3:오른쪽 4:왼쪽)
    shark_direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    graph = [[[] for _ in range(C)] for _ in range(R)]
    # 상어의 수 M만큼 상어의 정보가 주어짐.
    # z크기
    for _ in range(M):
        r, c, s, d, z = map(int, input().split())
        graph[r - 1][c - 1].append([s, d - 1, z])

    answer = 0
    catch_shark()
    print(answer)

#문제
#4 6 8
#4 1 3 3 8
#1 3 5 2 9
#2 4 8 4 1
#4 5 0 1 4
#3 3 1 2 7
#1 5 8 4 3
#3 6 2 1 2
#2 2 2 3 5
#22 답