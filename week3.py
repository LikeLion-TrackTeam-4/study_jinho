import sys

input = sys.stdin.readline

n = int(input())  # 건물 개수

backbuilding = []
count = 0
for i in range(0, n):
    now = int(input())  # 현재 건물 높이

    if len(backbuilding) == 0:
        backbuilding.append(now)
        continue

    else:  # 현재 건물을 바라볼 수 있는 건물이 있네?
        while len(backbuilding) > 0 and now >= backbuilding[-1]:  # 현재건물이 바로 뒤에있는거보다 큰가?
            backbuilding.pop()  # 현재 건물이 더 높으면 필요없으니 pop
        count += len(backbuilding)  # 현재 건물을 바라볼 수 있는 건물이 몇개인가
        backbuilding.append(now)  # 현재 건물도 이제 리스트로 들어가서 다음 건물과 비교 준비

print(count)