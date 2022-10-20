while True:
        bits = str(input("Введите 7 битов сообщения! Вводите осторожно:")).strip()
        failed = False
        if len(bits) != 7:
            print("Да не вводите вы столько символов, вводите 7!")
            failed = True
            continue
        
        for i in bits:
                  if i not in {'0', '1'}:
                      print("Да вводите вы только нолики и единички!")
                      failed = True
                      break
        if failed:
            continue
        print("Хорошие циферки - начинаю работу!")

        s1, s2, s3 = 0, 0, 0
        r1, r2, r3  = [int(bits[2**i - 1]) for i in range(3)]
        i1, i2, i3, i4 = map(int, [bits[2], bits[4], bits[5], bits[6]])


        s1 = (r1 + i1 + i2 + i4) % 2
        s2 = (r2 + i1 + i3 + i4) % 2
        s3 = (r3 + i2 + i3 + i4) % 2

        syn = str(s1) + str(s2) + str(s3)

        if syn == "000":
            print("Сообщение дошло без ошибок! Ура, товарищи!. Декодировано: ", ''.join( map(str, [i1, i2, i3, i4])))
        elif syn == "001":
            print("Ошибка допущена в бите r3! Информационные биты в порядке: ", ''.join( map(str, [i1, i2, i3, i4])))
        elif syn == "010":
            print("Ошибка допущена в бите r2! Информационные биты в порядке: ", ''.join( map(str, [i1, i2, i3, i4])))
        elif syn == "100":
            print("Ошибка допущена в бите r1! Информационные биты в порядке: ", ''.join( map(str, [i1, i2, i3, i4])))
        elif syn == "110":
            print("Ошибка допущена в бите i1! Исправленное сообщение: ", ''.join( map(str, [int(not(i1)), i2, i3, i4])))
        elif syn == "011":
            print("Ошибка допущена в бите i3! Исправленное сообщение: ", ''.join( map(str, [i1, i2, int(not(i3)), i4])))
        elif syn == "101":
            print("Ошибка допущена в бите i2! Исправленное сообщение: ", ''.join( map(str, [i1, int(not(i2)), i3, i4])))
        elif syn == "111":
            print("Ошибка допущена в бите i4! Исправленное сообщение:", ''.join( map(str, [i1, i2, i3, int(not(i4))])))

