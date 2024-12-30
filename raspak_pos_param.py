#ДЗ по уроку "Распаковка позиционных параметров

def print_param(a = 1000, b = 'по умолчанию', c= True ):
    #print("Печать из функции print_param")
    print(a, b, c)

#Вызов ф-ции  с разными параметрами
print("Аргументы при вызове: (1, 3, 10)")
print_param(1,3, 10)
print("Аргументы при вызове: (100)")
print_param(100)
print("Аргументы при вызове: ()")
print_param()
print("Аргументы при вызове: (b = 25)")
print_param(b=25)
print("Аргументы при вызове: c = [1, 3, 5]")
print_param(c=[1, 3, 5])

# Часть 2. Распаковка параметров
#Создаем список с 3-мя элементами
values_list = ["1", True, 3.14]
#Создаем словарь
values_dict = {"a":False, "b": 123, "c":"ABC"}

#Вызываем функцию с этими параметрами
print("Аргументы при вызове: ( *values_list, **values_dict) - nicht arbaiten")
#print_param(*values_list, **values_dict)    #не хочет, got multiple values for argument 'a'

# Часть 3. Распаковка + отдельные параметры
# Создаем список с 2-мя элементами
values_list2 = [5 + 2j, ['A', 'B', 'C']]
print("Аргументы при вызове: [5+2j], ['A', 'B', 'C']")
print_param(*values_list2)