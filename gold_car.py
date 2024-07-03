import re

def exclude_numbers(array, exclusions):
    return [num for num in array if num not in exclusions]

def exclude_by_digits(array, digit_position, digit_values):
    return [num for num in array if str(num).zfill(4)[digit_position] not in digit_values]

def main():
    # 1 ~ 10000 배열 생성
    numbers = list(range(1, 10001))

    # 사용자가 제외할 숫자 입력 받기
    user_exclusions = input("제외할 숫자들을 콤마 또는 띄어쓰기로 구분하여 입력하세요: ")
    if user_exclusions:
        exclusion_list = list(map(int, re.split(r'[,\s]+', user_exclusions.strip())))
        numbers = exclude_numbers(numbers, exclusion_list)

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
    sliced_numbers = numbers[min_display-1:max_display]

    # 남은 숫자 출력 (10개 단위로 끊어서 출력)
    print("남은 숫자들:")
    for i in range(0, len(sliced_numbers), 10):
        print(sliced_numbers[i:i+10])

if __name__ == "__main__":
    main()