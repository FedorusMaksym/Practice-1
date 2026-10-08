catalog = {
    1: ["Ноутбук", 26000, 5],
    2: ["Мишка", 450, 15],
    3: ["Клавіатура", 1200, 8]
}
cart = {}
get_price = lambda price: str(price) + "грн"
while True:
    print("1. Каталог")
    print("2. Додати в кошик")
    print("3. Переглянути кошик")
    print("4. Видалити з кошика")
    print("5. Купити")
    print("6. Адмінка (залишки)")
    print("0. Вихід")
    choice = input("Дія: ")
    if choice == "1":
        for item_id in catalog:
            item = catalog[item_id]
            print("ID:", item_id, "|", item[0], "| Ціна:", get_price(item[1]), "| На складі:", item[2])
    elif choice == "2":
        item_id = int(input("ID товару: "))
        if item_id in catalog:
            qty = int(input("Кількість: "))
            if qty <= catalog[item_id][2]:
                cart[item_id] = qty
                print("Додано.")
            else:
                print("Немає стільки на складі.")
        else:
            print("Немає такого товару.")
    elif choice == "3":
        total = 0
        for item_id in cart:
            qty = cart[item_id]
            name = catalog[item_id][0]
            price = catalog[item_id][1] * qty
            total = total + price
            print(name, "x", qty, "=", get_price(price))
        print("Разом:", get_price(total))

    elif choice == "4":
        item_id = int(input("ID товару для видалення: "))
        if item_id in cart:
            del cart[item_id]
            print("Видалено.")

    elif choice == "5":
        for item_id in cart:
            qty = cart[item_id]
            catalog[item_id][2] = catalog[item_id][2] - qty
        cart.clear()
        print("Куплено!")

    elif choice == "6":
        pas = input("Пароль: ")
        if pas == "admin":
            for item_id in catalog:
                item = catalog[item_id]
                print(item[0], "- Залишок:", item[2], "шт.")

    elif choice == "0":
        break