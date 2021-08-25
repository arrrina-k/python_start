total_sum = 0

list = [x ** 3 for x in range(1, 1000, 2)]
print(list)

for number in list:
    num = number
    digit_sum = 0
    while num != 0:
        digit_sum += num % 10
        num = num // 10
        remain_from_division = digit_sum % 7
    if remain_from_division == 0:
        total_sum += number
print(total_sum)

for number in list:
    number += 17
    num = number
    digit_sum = 0
    while num != 0:
        digit_sum += num % 10
        num = num // 10
        remain_from_division = digit_sum % 7
    if remain_from_division == 0:
        total_sum += number
print(total_sum)

