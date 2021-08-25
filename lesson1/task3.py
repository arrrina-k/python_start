list = [x for x in range(1, 101)]
for num in list:
    last_digit = num % 10
    if last_digit == 1 and num != 11:
        print(num, 'процент')
    elif last_digit >=2 and last_digit <= 4 and (num < 12 or num > 14):
        print(num, 'процента')
    else:
        print(num, 'процентов')
