from random import shuffle, randint

c, m = 'A23456789TJQK', '♥♣♦♠'
koloda = [i+j for i in c for j in m]
shuffle(koloda)

player_koloda = koloda[:4]
pig_koloda = koloda[4:8]

koloda = koloda[8:]

# print(koloda, player_koloda, pig_koloda)
player_sobral, pig_sobral = 0, 0

isPlayerHod = True

while True:
    player_koloda.sort()
    pig_koloda.sort()
    if player_sobral == 4:
        print('Вы выиграли!')
        print(f'Вы собрали {player_sobral} колоды. Мистер Свин собрал {pig_sobral} колоды')
        break
    elif pig_sobral == 4:
        print('Выиграл мистер свин!')
        print(f'Вы собрали {player_sobral} колоды. Мистер Свин собрал {pig_sobral} колоды')
        break
    print('Ваша колода')
    print(*player_koloda)
    # print(*pig_koloda)
    print()

    if isPlayerHod:
        player_nominals = [i[0] for i in player_koloda]
        print('Ваш ход: ')
        card = input('Введите карту: ').upper()
        while not card in player_nominals:
            print('У вас нет такой карты!')
            card = input('Введите карту: ')
        print('А у вас есть ' + card)
        if [i for i in pig_koloda if i[0] == card] != []:
            print('Мистер Свин: Да')
            xz = pig_koloda.copy()
            for i in xz:
                if i[0] == card:
                    pig_koloda.remove(i)
                    player_koloda.append(i)
        else:
            print('Мистер Свин: Нет, сэр, берите карту')
            player_koloda.append(koloda[0])
            koloda = koloda[1:]
            isPlayerHod = not isPlayerHod

        player_nominals = [i[0] for i in player_koloda]
        player_counts = [[i, player_nominals.count(i)] for i in list(set(player_nominals))]

        for i, count in player_counts:
            if count == 4:
                xz = player_koloda.copy()
                for k in xz:
                    if k[0] == i:
                        player_koloda.remove(k)
                player_sobral += 1
                print('Вы: Мне всегда везёт карточных играх!')
    else:
        print('Ход Мистера Свина: ')
        a = randint(0, len(pig_koloda)-1)
        card = pig_koloda[a][0]
        print('А у вас есть ' + card)
        if [i for i in player_koloda if i[0] == card] != []:
            print('Вы: Да')
            xz = player_koloda.copy()
            for i in xz:
                if i[0] == card:
                    player_koloda.remove(i)
                    pig_koloda.append(i)
        else:
            print('Вы: Нет, сэр, берите карту')
            pig_koloda.append(koloda[0])
            koloda = koloda[1:]
            isPlayerHod = not isPlayerHod

        pig_nominals = [i[0] for i in pig_koloda]
        pig_counts = [[i, pig_nominals.count(i)] for i in list(set(pig_nominals))]

        for i, count in pig_counts:
            if count == 4:
                xz = pig_koloda.copy()
                for k in xz:
                    if k[0] == i:
                        pig_koloda.remove(k)
                pig_sobral += 1
                print('Мистер Свин: Как же прекрасно!')
    print()
        
