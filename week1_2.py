#https://www.acmicpc.net/problem/25304
#첫째 줄에는 영수증에 적힌 총 금액 X가 주어진다.
#둘째 줄에는 영수증에 적힌 구매한 물건의 종류의 수 N이 주어진다.

#구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하면 Yes를 출력한다. 일치하지 않는다면 No를 출력한다.
x = int(input())
sum = 0

for _ in range(int(input())):
    a, b = map(int, input().split())
    sum += a * b

print("Yes") if sum == x else print("No")