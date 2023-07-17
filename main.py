import dictionary
random_word = dictionary.f(150, 327)
temp_word = "_"*len(random_word)
gametry = 6 # всего попыток(6)
word_try = len(random_word) #вспомогательный элемент, который нужен для функционала
part_body = ["голову", "туловище", "руку", "руку", "ногу", "ногу"]
list_temp_word = list(temp_word)
repit_word = list()
print(repit_word)

while gametry > 0:
    if ''.join(list_temp_word) == random_word:
        break
    print(''.join(list_temp_word))
    print("Неверные буквы\слова:", ','.join(repit_word))
    x_word = input("Введите букву или слово!\n")

    if len(x_word) > 1: # эта часть обрабатывает когда слово фул ввели
        if x_word == random_word:
            gametry = 0
            break
        else: 
            print("Не верно! Человек потерял", part_body[gametry])
            repit_word.append(x_word)
            gametry -= 1
    elif len(x_word) == 1:#когда буква
        if x_word in random_word:
            for i in range(len(random_word)):
                if x_word[0] == random_word[i]:
                    list_temp_word[i] = x_word[0]
                    word_try += 1
        
        elif x_word in repit_word:
            print("Вы уже писали это значение, попробуйте что-то другое!")

        else:

            gametry -= 1
            repit_word.append(x_word) 
            print("Не верно! Человек потерял", part_body[gametry])


if gametry == 0:
    print("Вы проиграли")
    exit            
else:
    print("Вы выиграли!")
    exit
