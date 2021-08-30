list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i in range(len(list)):
    if list[i][-1].isdigit() and int(list[i]) > 10:
        list[i] = '"' + str(list[i]) + '"'
    elif list[i][-1].isdigit() and int(list[i]) < 10:
        list[i] = '"' + '0' + str(list[i]) + '"'

sentence = ' '.join(list).replace("0+", "+0")
print(sentence)








