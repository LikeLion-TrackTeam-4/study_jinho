#https://www.acmicpc.net/problem/19644

#좀비떼가 기관총 진지에도 오다니
#좀비 담을 리스트 하나 만들어서
#count값 주고 count값이 길의 거리랑 같이지면 사망
#count값이 갈의거리보다 1적을때 쐈는데 못죽이면 지뢰를 격발하라
#지뢰 없으면 그때 죽는거
def survive():
    L = int(input())  # 1 길의거리 6m
    ML, MK = map(int, input().split())  # 2 총의 사거리3 사거리내 데미지2
    Cammo = int(input())  # 3 수평 세열 지향성 지뢰 1개
    zombies = [0] + list(map(int, input().split()))  # 4 부터 쭉 쫨비

    for i in range(1, L + 1):
        damage = ML * MK  # 현재 위치에서의 총 데미지 계산 (모든 좀비에게 관통)
        zombies[i] -= damage  # 현재 위치의 좀비 체력을 감소시킴
        if zombies[i] <= 0:
            # 좀비를 제거하고 길을 한 칸 앞으로 이동
            zombies.pop(i)
            L -= 1
            i -= 1
        if i == 0:
            # 1미터 앞에 좀비가 존재하는 경우 지뢰 사용
            if Cammo == 0:
                return "NO"
            else:
                zombies.pop(0)
                Cammo -= 1
    return "YES"

result = survive()
print(result)
