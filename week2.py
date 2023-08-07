# https://www.acmicpc.net/problem/5397

# 예제입력            #예제출력
# 2                 #BAPC
# <<BP<A>>Cd-       #ThIsIsS3Cr3t
# ThIsIsS3Cr3t

import sys

num = int(sys.stdin.readline())

for i in range(num):
    password = list(sys.stdin.readline().strip())#공백제거
    left, right = [], [] #커서를 기준으로 왼쪽 문자열은 left, 오른쪽 문자열은 right에 담는 방식

    for word in password:
        if word == '<':
            if left:  # left가 비어있지 않으면 -> 커서가 이동가능하면
                right.append(left.pop())
        elif word == '>':
            if right:  # 커서가 이동가능하면
                left.append(right.pop())
        elif word == '-':
            if left:  # 삭제할 문제가 있으면
                left.pop()
        else:
            left.append(word)

    left.extend(reversed(right))

    print(''.join(left))
