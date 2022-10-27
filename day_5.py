# users= {
#     'sul': 123 
# }
# l = input('Введите имя: ')
# p = input('Введите пороль: ')

# if l in users:
#     print ("Пользователь с таким логином уже существуюет")
# else:
#     users[l] = p
# print (users)

# 12
# his_her_friends = {
#     'Lyazat',
#     'Salavat',
#     'Daniyar',
#     'Bolot',
#     'Alymbek',
#     'Dastan',
#     'Maksat',
#     'Adinai',
# }

# my_friends = {
#     "Joomart",
#     "Adinai",
#     "Ermek",
#     'Bolot',
#     'Alymbek',
#     'Dastan',
#     "Atai",
#     "Alymbek",
# }
# our_f = (his_her_friends.intersection(my_friends))

# print (our_f)


# 11
# my_friends = {
#     "Joomart": "+77555246810",
#     "Adinai": "+77555013579",
#     "Ermek": "+77777013579",
#     "Atai": "+77777246810",
#     "Alymbek": "+77555501234",
# }

# his_her_friends = {
#     "Lyazat": "+77551123456",
#     "Salavat": "+77552234567",
#     "Daniyar": "+77553345678",
#     "Bolot": "+77554456789",
#     "Alymbek": "+77555501234",
#     "Dastan": "+77556678912",
#     "Maksat": "+77557789012",
#     "Adinai": "+77555013579",
# }
# our_friends = {}

# our_friends.update(my_friends)
# our_friends.update(his_her_friends)

# pprint(our_friends)

# 10
# suitcase = []
# suitcase.append('вещ1')
# suitcase.append('вещ2')
# suitcase.append('вещ3')
# suitcase.append('вещ4')
# suitcase.append('вещ5')
# suitcase.pop(4)

# print(suitcase)

# 9
# south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 
#   'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
# a = set()
# a.update(south_american_countries)
# print (a)

# 8
# k = set()
# a = int (input('Введите число: '))
# b = int (input('Введите число: '))
# c = int (input('Введите число: '))
# d = int (input('Введите число: '))
# e = int (input('Введите число: '))
# f = int (input('Введите число: '))
# g = int (input('Введите число: '))
# h = int (input('Введите число: '))
# i = int (input('Введите число: '))
# j = int (input('Введите число: '))
# k.update([a, b, c, d, e, f ,g, h, i, j ])
# k = tuple(k)
# print (k)

# 7
# work = {
#     'user1': {
#         'name': 'Sultan', 
#         'proffession': 'IT'
#         },
#     'user2': {
#         'name': 'Asan', 
#         'proffession': 'Teacher'
#         },
#     'user3': {
#         'name': 'Ali', 
#         'proffession': 'Reziser'
#         },
#     'user4': {
#         'name': 'Malika', 
#         'proffession': 'Advokat'
#         },
#     'user5': {
#         'name': 'Amir', 
#         'proffession': 'IT2'
#         },        
#     }

# print(f'Здравствуйте {work["user1"]["name"]} Прекрасная профессия {work["user1"]["proffession"]} ')
# print(f'Здравствуйте {work["user2"]["name"]} Прекрасная профессия {work["user2"]["proffession"]} ')
# print(f'Здравствуйте {work["user3"]["name"]} Прекрасная профессия {work["user3"]["proffession"]} ')
# print(f'Здравствуйте {work["user4"]["name"]} Прекрасная профессия {work["user4"]["proffession"]} ')
# print(f'Здравствуйте {work["user5"]["name"]} Прекрасная профессия {work["user5"]["proffession"]} ')

# 6
# users = {}
# l = input('Введите имя: ')
# p = input('Введите попроль: ')
# users[l] = p

# ll = input('Введите имя: ')
# pp = input('Введите попроль: ')
# users[ll] = p

# l1 = input('Введите имя: ')
# p1 = input('Введите попроль: ')
# users[l1] = p1

# print (users)

# 4
# # Меню №1:
# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
# menu['besh_barmak'] = 130
# menu.update ({'lagman': 135})
# menu.pop('borsh')

# menu['drinks'] = ['Coca-Cola', 'Sprite', 'Fanta']

# print (menu)

# 3
# a = {12, 15, 18, 10, 7}
# a.add(4)
# a.pop()
# print (a)

# 2
# # Множество № 2:
# farm_1 = {"dog", "cat", "mouse", "sheep"}
 
# # Множество № 3:
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
 
# print (farm_2.difference(farm_1))

# 1
# # Множество № 2:
# farm_1 = {"dog", "cat", "mouse", "sheep"}
 
# # Множество № 3:
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}

# print (farm_1.intersection(farm_2))

# 0
# Множество № 1:
# dates_of_birth = {3,10,11,13,31,21,1,10,3,5,6,6}
# dates_of_birth.remove (11)
# print(dates_of_birth)


# a = {1212, 43, 789.678, 90, 89}
# методы удаления
# a.remove(89)
# a.pop()
# a.clear()
# a.discard(1233123)
# print(a)


# методы добавления
# a.add(14)
# a.update([1,23,4,5])

# методы сравнения
# a = {1212, 43, 90, 89}
# b = {12, 4, 90, 89}

# Возрвращает объекты которые есть и во множестве a и b
# print(a)
# print(a.intersection(b))

# # Удаления всех не похожих объектов
# a.intersection_update(b)
# print(a)

# Возрвращает объекты a которые нет в b
# print(a.difference(b))




# from pprint import pprint


# a = {213:123, 'key': 'value'}

# Методы добавления
# a['new'] = 145
# a['key'] = {'run': True}
# a['key2'] = {'run': True}

# a.update({'run': True})

# a = {
#     'key': 'value',
#     'key2': {'run': True},
#     'key3': {'run3': True},
    # }
# Методы получения

# print(a.get('key3'))
# print(a['key3'])

# print(a.keys())
# print(a.values())
# print(a.items())

# a.clear()
# print(a)





# С множествами можно выполнять множество операций: находить объединение, пересечение...

# len(s) - число элементов в множестве (размер множества).
# x in s - принадлежит ли x множеству s.
# set.isdisjoint(other) - истина, если set и other не имеют общих элементов.
# set == other - все элементы set принадлежат other, все элементы other принадлежат set.
# set.issubset(other) или set <= other - все элементы set принадлежат other.
# set.issuperset(other) или set >= other - аналогично.
# set.union(other, ...) или set | other | ... - объединение нескольких множеств.
# set.intersection(other, ...) или set & other & ... - пересечение.
# set.difference(other, ...) или set - other - ... - множество из всех элементов set, не принадлежащие ни одному из other.
# set.symmetric_difference(other); set ^ other - множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих.
# set.copy() - копия множества.
# И операции, непосредственно изменяющие множество:

# set.update(other, ...); set |= other | ... - объединение.
# set.intersection_update(other, ...); set &= other & ... - пересечение.
# set.difference_update(other, ...); set -= other | ... - вычитание.
# set.symmetric_difference_update(other); set ^= other - множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих.
# set.add(elem) - добавляет элемент в множество.
# set.remove(elem) - удаляет элемент из множества. KeyError, если такого элемента не существует.
# set.discard(elem) - удаляет элемент, если он находится в множестве.
# set.pop() - удаляет первый элемент из множества. Так как множества не упорядочены, нельзя точно сказать, какой элемент будет первым.
# set.clear() - очистка множества.
