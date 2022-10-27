marks = {'Bill': None,'Jane': None,'John': None,'Mary': None}
marks['Bill'] = int(input('Enter mark for Bill: '))
marks['Jane'] = int(input('Enter mark for Jane: '))
marks['John'] = int(input('Enter mark for John: '))
marks['Mary'] = int(input('Enter mark for Mary: '))
average = marks['Bill'] + marks['Jane'] + marks['John'] + marks['Mary']
print(f'Average mark: {average // 2}')




# 11
# num_1 = int(input('Введите первое число: ')) 
# num_2 = int(input('Введите второе число: ')) 
# oper = (input('выберете операцию(+, -, *, /, //, %): '))
# if oper == '+':
#     print(f'результат:\n>{num_1 + num_2}')
# elif oper == '-':
#     print(f'результат:\n>{num_1 - num_2}')
# elif oper =='*':
#     print(f'результат:\n>{num_1 * num_2}')

# if num_2 !=  0:
#     if oper == '/':
#         print(f'результат:\n>{num_1} {oper} {num_2} = {num_1 / num_2}')      
#     elif oper == '//':
#         print(f'результат:\n>{num_1 // num_2}')   
#     elif oper == '%':
#         print(f'результат:\n>{num_1 % num_2}')    
# else:
#     print('на 0 делить нельзя')




# 12
# wather_dict = {'base': 'stations',
#  'clouds': {'all': 100},
#  'datetime': '2022-10-26 11:33:21.774524',
#  'main': {'feels_like': 6.57,
#           'grnd_level': 925,
#           'humidity': 71,
#           'pressure': 1022,
#           'sea_level': 1022,
#           'temp': 9.18,
#           'temp_max': 9.18,
#           'temp_min': 9.18},
#  'name': 'Almaty',
#  'rain': {'1h': 1.26},
#  'sys': {'country': 'KZ', 'sunrise': 1666747131, 'sunset': 1666785198},
#  'timezone': 21600,
#  'visibility': 10000,
#  'weather': [{'description': 'moderate rain',
#               'icon': '10d',
#               'id': 501,
#               'main': 'Rain'}],
#  'wind': {'deg': 262, 'gust': 9.09, 'speed': 4.99}}

# for i in wather_dict['weather']:
#     q = (i['description'])

# print (f'''
# Дата: {wather_dict['datetime'][:10]}
# # Время: {wather_dict['datetime'][11:16]}
# # Погода в городе:{wather_dict['name']}  
# # Температура: {wather_dict['main']['temp']}°C  
# # Описание: {q} 
# # Облачность: {wather_dict['clouds']['all']} 
# # Влажность: {wather_dict['main']['humidity']} 
# # Давление: {wather_dict['main']['pressure']}  мм.рт.ст 
# # Скорость ветра: {wather_dict['wind']['speed']} 
# ''')

#3 
# a = 2897607 
# if a % 3 == 0 :
#     b = (a // 3) * (a // 3)
# else :
#     print ('2897607 не делиться на 3 без остатка')
# k = str(b)
# c = len(k)

# if c > 10 :
#     f = k.replace('3' , '0')
# print (f[:6])

# 7
# print ('Enter two strings')
# a = input('Enter first string: ')
# b = input('Enter second string: ')
# c = len(a)
# d = len(b)
# if c > d :
#     e = (c - d)
#     print (f'firs string is longer by {e} characters')
# elif d > c :
#     f = (d - c)
#     print (f'second string is longer by {f} characters')
# else:
#     print (f'Strings are equal length')