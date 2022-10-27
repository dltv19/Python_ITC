# points = [0] 
# s = int (input (""" 
# сколько будет 5 + 5 
# а) 12
# b) 10
# c) 14 
# ответ : """ ))

# p = int (input (""" 
# сколько будет 6 + 6 
# а) 12
# b) 10
# c) 14 
# ответ : """ ))

# q = int (input (""" 
# сколько будет 7 + 7 
# а) 12
# b) 10
# c) 14 
# ответ : """ ))

# m = int (input (""" 
# сколько будет 3 + 3 
# а) 5
# b) 6
# c) 7 
# ответ : """ ))

# k = int (input (""" 
# сколько будет 4 + 5 
# а) 9
# b) 10
# c) 11 
# ответ : """ ))

# if p ==  12:
#     points.pop(0)
#     points.append(1)
#     print (f'баллы: + 1')
# if p != 12:
#     po

# if  ==  10:
#     points.pop(0)
#     points.append(1)
#     print (f'баллы: + 1')
# if s != 10:
#     print (f'баллы: 0')




# users = [('kiri', '12345'), ('azat', '121212')]
# l = input('Введите логин: ')
# p = input('Введите пароль: ')
# pp = input('Подтвердите пароль: ')


# if not l.isalpha() and not l.isdigit():
#     print('Логин верный.')
#     if p == pp:
#         print('Пароль верный.')
#         user = (l, p)
#         users.append(user)
#     else:
#         print('Пароль должен совпадать с подтверждением пароля.')  
# else:
#     print('Логин должен содержать буквы и цифры.')

# print(users)


# products = [
#   'яблоко', 
#   'груша', 
#   'арбуз',
#   'банан', 
#   'мандарин']
# print ("""
# o. яблоко 
# 1. груша 
# 2. арбуз
# 3. банан 
# 4. мандарин""")
# f = int (input ('выберете индекс товара: ' ))
# if f >= 0 and f <= 4 :
#     products.pop(f)
# else : 
#     print ('Индекс введен неправильно')
# print (products)



# products = [
#   'яблоко', 
#   'груша', 
#   'арбуз',
#   'банан', 
#   'мандарин'
# ]
# a = products.index('яблоко')
# b = products.index('груша')
# c = products.index('арбуз')
# d = products.index('банан')
# e = products.index('мандарин')
# print ("""
# o. яблоко 
# 1. груша 
# 2. арбуз
# 3. банан 
# 4. мандарин""")
# f = int (input ('выберете индекс товара: ' ))
# if f == 0:
#     products.pop(a)
# if f == 1:
#      products.pop(b)
# if f == 2:
#      products.pop(c)
# if f == 3:
#      products.pop(d)
# if f == 4:
#      products.pop(e)
# if  0 < f > 4:
#     print ('введен не правельный индекс')
# print (products)


# list = []
# a = int (input ('>>> '))
# b = int (input ('>>> '))
# c = int (input ('>>> '))
# d = int (input ('>>> '))
# e = int (input ('>>> '))
# list.append(a)
# list.append(b)
# list.append(c)
# list.append(d)
# list.append(e)
# f = max(list)
# g = min(list)
# h = sum(list)
# srednee = h / len(list)
# print(f"максимальное число: {f}, минемальное число: {g}, среднее: {srednee}")



# list_1 = []
# list_2 = []
# a = int (input ('>>> '))
# b = int (input ('>>> '))
# c = int (input ('>>> '))
# d = int (input ('>>> '))
# e = int (input ('>>> '))

# if a % 2 == 0:
#     list_1.append(a)
# else:
#     list_2.append(a)
# if b % 2 == 0:
#     list_1.append(b)
# else:
#     list_2.append(b)
# if c % 2 == 0:
#     list_1.append(c)
# else:
#     list_2.append(c)
# if d % 2 == 0:
#     list_1.append(d)
# else:
#     list_2.append(d)
# if e % 2 == 0:
#     list_1.append(e)
# else:
#     list_2.append(e)

# print (list_1)
# print (list_2)



#9
# numbers = [123, 321, 2, 543]
# a = sum(numbers)
# print (a)
# print (numbers[0] * numbers[1] * numbers[2] * numbers[3])

#8
# python_list = ["int", "str", "bool", "if", "else", "elif", "loop", "tuple", "list", "None", True, False]
# a = python_list.index('loop')
# python_list.pop(a)
# print (python_list)

#7
# a = []
# a.append('Sultan')
# a.append(2005)
# a.append('Python')
# print (a)

#6
# names = ['Jack', 'Jimmy', 'Oskar', 'Jhon', 'Jackson', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon']
# names.remove('Oskar')
# print (names)

#5
# names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon']
# print (names.count('Jack'))

# 4
# a = [1, 1.5, 'hello']
# b = [18, 22.9, 'world', True]
# a.extend(b)
# print (a)

# 3
# a = ['Sultan', 'Asan', 'Ali','Abylai', 'Mailika' ]
# c1 = ''.join(a)
# print (c1)

# 2
# a = ['hello', 17, 19.5, True, [1, 2, 3]]

# 1
# b = (1 ,2 ,3)
# print (b [0])
# print (b [1])
# print (b [2])


# 0
# a = []
# a.append('hello')
# a.append(20)
# a.append(18.7)
# a.append(True)
# a.append([1, 2, 3])
# print (a)

# a = []
# # а пустой лист 
# print (type(a))
# b = ['hello', 12, 1.9, True, [1, 2, 3, 5]]
# print (b[::-1])
# print(b[4] [2])


# print(a[::-1])
# print(a[4][2])

# c = a.count(12)
# print(c)
# a = ['hello', 12, 1.9, 'hello', True, [1, 2, 4, 5], 12]
# print(a)
# a.append(1)

# print(a)
# a.remove('hello')
# a.remove('hello')
# print(a)


# a = ['hello', 12, 1.9, 'hello', True, [1, 2, 4, 5], 12]

# s = a.index(1.9)
# a.pop(s)
# print(a)

# a = [1, 2, 3, 4, 5, 6]
# b = [7, 8, 9, 10, 11, 12]

# a.extend(b)
# print(a + b)

# a = [1, 7, 8, 9, 1, 0, 11, 1, 2, 2, 3, 4, 5, 6]
# a.sort(reverse=True)
# print(a)

# max 
# min
# sum