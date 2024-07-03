import re
import random


def read_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return list(map(int, re.split(r'[,\s]+', content.strip())))


def exclude_numbers(array, exclusions):
    exclusion_set = set(exclusions)
    return [num for num in array if num not in exclusion_set]


def exclude_by_digits(array, digit_position, digit_values):
    digit_values_set = set(digit_values)
    return [num for num in array if str(num).zfill(4)[digit_position] not in digit_values_set]


def main():
    # 1 ~ 10000 배열 생성
    numbers = list(range(1, 10001))

    # gold_car.txt에서 숫자 읽기
    exclusions = read_numbers_from_file('gold_car.txt')
    numbers = exclude_numbers(numbers, exclusions)

    # 자리수와 값을 입력받아 제외 (천의 자리)
    digit_positions = {1: 0, 2: 1, 3: 2, 4: 3}  # 천, 백, 십, 일의 자리 인덱스

    exclude_digits_input = input("제외할 천의 자리 숫자들을 콤마 또는 띄어쓰기로 구분하여 입력하세요 (예: 1, 2, 3): ")
    if exclude_digits_input:
        exclude_digits_list = re.split(r'[,\s]+', exclude_digits_input.strip())
        numbers = exclude_by_digits(numbers, digit_positions[1], exclude_digits_list)

    # 자리수와 값을 입력받아 제외 (백의 자리)
    exclude_digits_input = input("제외할 백의 자리 숫자들을 콤마 또는 띄어쓰기로 구분하여 입력하세요 (예: 4, 5, 6): ")
    if exclude_digits_input:
        exclude_digits_list = re.split(r'[,\s]+', exclude_digits_input.strip())
        numbers = exclude_by_digits(numbers, digit_positions[2], exclude_digits_list)

    # 최소 및 최대 출력 숫자 범위 입력 받기
    min_display = int(input("몇 번 이상의 숫자를 보시겠습니까? "))
    max_display = int(input("몇 번 이하의 숫자를 보시겠습니까? "))

    # 범위에 맞게 숫자 슬라이싱
    sliced_numbers = numbers[min_display - 1:max_display]

    # 남은 숫자 출력 (10개 단위로 끊어서 출력)
    print("남은 숫자들:")
    for i in range(0, len(sliced_numbers), 10):
        print(sliced_numbers[i:i + 10])

    # 랜덤으로 몇 개의 숫자를 뽑을지 입력 받기
    num_random = int(input("랜덤으로 몇 개의 숫자를 뽑아드릴까요? "))
    if num_random > len(sliced_numbers):
        print(f"남은 숫자가 {len(sliced_numbers)}개 뿐입니다. 모두 출력합니다.")
        num_random = len(sliced_numbers)

    random_numbers = random.sample(sliced_numbers, num_random)

    # 랜덤으로 뽑힌 숫자 출력
    print("랜덤으로 뽑힌 숫자들:")
    print(random_numbers)


if __name__ == "__main__":
    main()
