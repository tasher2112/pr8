sum = 0
while(True):
    flag = False
    x = input("Введите цифру, или stop/end для выхода из цикла:")
    if x == "stop" or x == "end":
        print("Сумма всех ранее ввёденных цифер:", sum)
        break
    else:
        for i in x:
            if i == ".":
                continue
            elif i.isdigit() == False:
                print("Неверный ввод! Повторите ещё раз!")
                flag = True
                continue
        if flag == False:
            sum += float(x)
        else:
            flag == False