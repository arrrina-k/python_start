def num_translate(eng_num):
    print(eng_dict.get(eng_num))


eng_num = input('Введите число от 1 до 10 на английском: ')

eng_dict = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
}
num_translate(eng_num)
