"""
Использование параметров *args/**kwargs
Задача "Однокоренные"
Функция single_root_words принимает одно обязательное слово
в параметр root_word, а далее неограниченную последовательность
в параметр *other_words. Функция должна составить
новый список same_words только из тех слов списка other_words,
которые содержат root_word или наоборот root_word содержит
одно из этих слов.
"""
def single_root_words(root_word, *other_words):
    same_words=[]   #список слов, которые содержат root_word или наоборот
    len_list = len(other_words)  #длина списка same_words
    for i in range (len_list):
        element=other_words[i]   #берем очередной элемент списка other_words[i]
        element=element.lower()  #переводим в нижний регистр его и root_word
        root_word=root_word.lower()
        #Сравниваем element и root_word на вхождение друг в друга
        #Если TRUE, добавляем текущий элемент
        # из other_words в список same_words
        if ((element.count(root_word) != 0) or (root_word.count(element) != 0)):
            same_words.append(other_words[i])
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)