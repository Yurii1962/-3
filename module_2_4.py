"""
ДЗ по уроку "Цикл for. Элементы списка. Полезные функции в цикле"
Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Используя этот список, составьте второй список primes,
содержащий только простые числа.
А так же третий список not_primes, содержащий все не простые числа.
"""
#исходный список
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

#список простых чисел
primes = []
#список непростых чисел
not_primes = []

#длина исходного списка numbers
len_numbers = len(numbers)

for i in range(len_numbers):
    signal = False      #сигнал "Число уже внесено в список?"
    for j in range(i):
        #print(f"  i = {i} j = {j}")
        if j >=2:
            if (numbers[i]%j == 0):
                signal = True
    if signal == False:
        primes.append(numbers[i])   #вносим в список простых
    else:
        not_primes.append(numbers[i])   #вносим в список НЕпростых

print(not_primes)
print(primes)