"""Написать программу, которая:
- Запрашивает у пользователя количество строк. (должна быть проверка)
- Затем сами строки.
- Определяет, сколько различных слов содержится в этом тексте, и выводит их количество

Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки."""
numberOfLines=int(input("Введите кол-во строк: "))

text=""

if numberOfLines<=0:
    print("Введенные данные должны быть числом больше нуля")
else:
    for i in range(1, numberOfLines+1):
        str=input("Введите строку: ")
        text=text+str+" "
print(text)
text=text.split()
text=set(text)
print("Кол-во различных слов в тексте: ", len(text))