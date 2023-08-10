# https://www.acmicpc.net/problem/15815
import sys
#후위 연산식을 중위연산식으로 바꿔 계산하는 문제입니다.
#스택을 구현해보는 필수 자료구조라고 생각합니다!

answer = sys.stdin.readline().strip()
result = 0
stack = []

for i in answer:
    if i == '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(a + b)
    elif i == '*':
        a = stack.pop()
        b = stack.pop()
        stack.append(a * b)
    elif i == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(b - a)
    elif i == '/':
        a = stack.pop()
        b = stack.pop()
        stack.append(b // a)
    else:
        stack.append(int(i))

for j in stack:
    print(j)
