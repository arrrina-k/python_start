staff = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
names = []

for i in range(len(staff)):
    information = staff[i].split()
    names.append(information[-1])

for i in range(len(names)):
   names[i] = names[i].title()
   print('Привет, {}!'.format(names[i]))


