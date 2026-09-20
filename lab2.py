login = input("Введіть логін: ")
password = input("Введіть пароль: ")
if login == "user1" and password == "1111":
    grades = [10, 8, 4, 12, 3, 9]
elif login == "user2" and password == "2222":
    grades = [5, 6, 7, 8, 9, 10, 8]
elif login == "user3" and password == "3333":
    grades = [2, 3, 4, 1, 4, 2, 3]
elif login == "user4" and password == "4444":
    grades = [12, 11, 4, 5, 2, 8, 10]
else:
    grades = None
    
if grades != None:
    print("Успішний вхід!")
    print("Ваші оцінки:", grades)

    good_count = 0
    bad_count = 0
    for grade in grades:
        if grade >= 5:
            good_count += 1
        else:
            bad_count += 1

    print("Задовільні оцінки (5-12):", good_count)
    print("Незадовільні оцінки (1-4):", bad_count)

else:
    print("Невірний логін або пароль!")