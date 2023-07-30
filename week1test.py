import sys

# 오늘로부터 N+1되는날퇴사
# 남은 N일간 최대한 많은 상담

n = int(input())  # 퇴사까지 남은 일수
# 두가지를 배열로 만들어서 0으로 채워놓는다
T = [0 for i in range(n + 1)]  # 상담을 완료하는데 걸리는 기간 T
P = [0 for i in range(n + 1)]  # 상담으로 버는 돈 P
# money[i]는 i번째 날까지 일 할경우 최대값
money = [0 for i in range(n + 1)]

for i in range(n):
    T[i], P[i] = map(int, input().split())

for i in range(n-1, -1, -1):  # 역순으로 진행
    if T[i] + i <= n:  # 일수를 넘는지 확인
        money[i] = max(P[i] + money[i + T[i]], money[i+1])
    else:
        money[i] = money[i+1] #일수가 넘어갔으면

print(money[0])
