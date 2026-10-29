import random

PREFIXES = [
    "Срібний", "Золотий", "Тіньовий", "Місячний", "Сонячний",
    "Крижаний", "Вогняний", "Бурштиновий", "Смарагдовий", "Рубіновий",
    "Сапфіровий", "Дикий", "Стародавній", "Містичний", "Зоряний",
    "Похмурий", "Світлий", "Зачарований", "Драконячий", "Лісовий"
]
NOUNS = [
    "корінь", "лист", "цвіт", "гриб", "плід",
    "пелюстка", "пилок", "кристал", "камінь", "мох"
]

INGREDIENTS = [f"{prefix} {noun}" for prefix in PREFIXES for noun in NOUNS]

POTION_NAMES = [
    "Зілля здоров'я", "Мале зілля здоров'я", "Велике зілля здоров'я",
    "Зілля мани", "Мале зілля мани", "Велике зілля мани",
    "Зілля сили", "Зілля спритності", "Зілля мудрості", "Зілля витривалості",
    "Зілля невидимості", "Зілля нічного зору", "Зілля вогню", "Зілля льоду",
    "Зілля блискавки", "Зілля захисту", "Зілля швидкості", "Зілля удачі",
    "Зілля зцілення", "Зілля очищення", "Еліксир життя", "Еліксир молодості",
    "Еліксир знань", "Еліксир хоробрості", "Еліксир спокою", "Зілля сну",
    "Зілля пробудження", "Зілля кам'яної шкіри", "Зілля водного дихання",
    "Зілля стрибка", "Зілля левітації", "Зілля телепортації", "Зілля відваги",
    "Зілля концентрації", "Зілля відновлення", "Зілля захисту від отрути",
    "Зілля отрути", "Зілля слабкості", "Зілля хаосу", "Зілля гармонії",
    "Зілля міцності", "Зілля ясності", "Зілля духу", "Зілля дракона",
    "Зілля фенікса", "Зілля місячного сяйва", "Зілля зоряного пилу",
    "Зілля вічного полум'я", "Королівський еліксир",
    "Еліксир Великого алхіміка"
]

POTIONS = {}
for i, name in enumerate(POTION_NAMES):
    first = INGREDIENTS[(i * 3) % len(INGREDIENTS)]
    second = INGREDIENTS[(i * 7 + 11) % len(INGREDIENTS)]
    if first == second:
        second = INGREDIENTS[(i * 7 + 12) % len(INGREDIENTS)]
    POTIONS[name] = {
        "recipe": {first: 2, second: 1},
        "price": 25 + i * 7
    }


class Player:
    def __init__(self):
        self.gold = 100
        self.day = 1
        self.max_days = 30
        self.ingredients = {}
        self.potions = {}

    def ingredient_slots(self):
        return sum(1 for amount in self.ingredients.values() if amount > 0)

    def potion_slots(self):
        return sum((amount + 9) // 10 for amount in self.potions.values() if amount > 0)

    def add_ingredient(self, name, amount):
        try:
            current = self.ingredients.get(name, 0)
            if current + amount > 25:
                print("У слоті інгредієнта максимум 25 одиниць.")
                return False
            if current == 0 and self.ingredient_slots() >= 25:
                print("Інвентар інгредієнтів заповнений!")
                return False
            self.ingredients[name] = current + amount
            return True
        except Exception as error:
            print(f"Помилка інвентаря: {error}")
            return False

    def add_potion(self, name):
        try:
            current = self.potions.get(name, 0)
            old_slots = (current + 9) // 10
            new_slots = (current + 1 + 9) // 10
            if self.potion_slots() - old_slots + new_slots > 10:
                print("Інвентар зіль заповнений!")
                return False
            self.potions[name] = current + 1
            return True
        except Exception as error:
            print(f"Помилка додавання зілля: {error}")
            return False

    def show_inventory(self):
        try:
            print("\n--- ІНГРЕДІЄНТИ ---")
            for name, amount in self.ingredients.items():
                print(f"{name}: {amount}/25")
            if not self.ingredients:
                print("Порожньо")
            print(f"Зайнято слотів: {self.ingredient_slots()}/25")

            print("\n--- ЗІЛЛЯ ---")
            for name, amount in self.potions.items():
                print(f"{name}: {amount} шт.")
            if not self.potions:
                print("Порожньо")
            print(f"Зайнято слотів: {self.potion_slots()}/10")
            print(f"Золото: {self.gold}")
        except Exception as error:
            print(f"Помилка показу інвентаря: {error}")


def show_recipes():
    try:
        print("\n--- РЕЦЕПТИ ЗІЛЬ ---")
        for i, (name, data) in enumerate(POTIONS.items(), 1):
            recipe = ", ".join(
                f"{ingredient} x{amount}"
                for ingredient, amount in data["recipe"].items()
            )
            print(f"{i}. {name} | {recipe} | Ціна: {data['price']} золота")
    except Exception as error:
        print(f"Помилка рецептів: {error}")


def craft_potion(player):
    try:
        show_recipes()
        choice = input("Номер зілля (0 — назад): ").strip()
        if choice == "0":
            return
        index = int(choice) - 1
        names = list(POTIONS.keys())
        if index < 0 or index >= len(names):
            print("Неправильний номер рецепта.")
            return

        name = names[index]
        recipe = POTIONS[name]["recipe"]

        for ingredient, amount in recipe.items():
            if player.ingredients.get(ingredient, 0) < amount:
                print(f"Недостатньо інгредієнта: {ingredient}.")
                return

        if not player.add_potion(name):
            return

        for ingredient, amount in recipe.items():
            player.ingredients[ingredient] -= amount
            if player.ingredients[ingredient] == 0:
                del player.ingredients[ingredient]

        print(f"Ти створив зілля: {name}!")
    except ValueError:
        print("Введи номер цифрами.")
    except Exception as error:
        print(f"Помилка створення зілля: {error}")


def sell_potions(player):
    try:
        available = [(name, amount) for name, amount in player.potions.items() if amount > 0]
        if not available:
            print("У тебе немає зіль для продажу.")
            return

        print("\n--- КРАМНИЦЯ ---")
        for i, (name, amount) in enumerate(available, 1):
            print(f"{i}. {name} x{amount} — {POTIONS[name]['price']} золота за штуку")
        print("0. Назад")
        choice = input("Введи номер зілля або 'все': ").strip().lower()

        if choice == "0":
            return
        if choice == "все":
            total = 0
            for name, amount in available:
                total += POTIONS[name]["price"] * amount
                player.potions[name] = 0
            player.gold += total
            print(f"Продано всі зілля за {total} золота.")
            return

        index = int(choice) - 1
        if index < 0 or index >= len(available):
            print("Неправильний номер.")
            return

        name, amount = available[index]
        quantity = int(input(f"Скільки продати (1-{amount})? "))
        if quantity < 1 or quantity > amount:
            print("Неправильна кількість.")
            return

        total = POTIONS[name]["price"] * quantity
        player.potions[name] -= quantity
        player.gold += total
        print(f"Продано {name} x{quantity}. Отримано {total} золота.")
    except ValueError:
        print("Введи правильний номер і кількість.")
    except Exception as error:
        print(f"Помилка продажу: {error}")


def start_day(player):
    try:
        print(f"\n========== ДЕНЬ {player.day}/{player.max_days} ==========")
        received = 0
        attempts = 0
        while received < 5 and attempts < 100:
            attempts += 1
            ingredient = random.choice(INGREDIENTS)
            amount = random.randint(1, 3)
            if player.add_ingredient(ingredient, amount):
                print(f"Знайдено: {ingredient} x{amount}")
                received += 1
        if received < 5:
            print("Інвентар переповнений: отримано менше ніж 5 інгредієнтів.")
    except Exception as error:
        print(f"Помилка початку дня: {error}")


def finish_day(player):
    try:
        print(f"\nДень завершено. Твоє золото: {player.gold}")
        player.day += 1
    except Exception as error:
        print(f"Помилка завершення дня: {error}")


def main():
    try:
        player = Player()
        print("=" * 45)
        print("       АЛХІМІК: ШЛЯХ ДО МАЙСТЕРСТВА")
        print("=" * 45)
        print("Ти — алхімік. У тебе є 30 днів, щоб накопичити")
        print("10 000 золотих і стати Великим алхіміком.")

        while player.day <= player.max_days:
            if player.gold >= 10000:
                print("\nПЕРЕМОГА! Ти став Великим алхіміком!")
                return

            start_day(player)
            day_finished = False

            while not day_finished:
                try:
                    print("\n1. Інвентар")
                    print("2. Переглянути рецепти")
                    print("3. Створити зілля")
                    print("4. Продати зілля")
                    print("5. Завершити день")
                    print("0. Вийти з гри")
                    choice = input("Твій вибір: ").strip()

                    if choice == "1":
                        player.show_inventory()
                    elif choice == "2":
                        show_recipes()
                    elif choice == "3":
                        craft_potion(player)
                    elif choice == "4":
                        sell_potions(player)
                    elif choice == "5":
                        finish_day(player)
                        day_finished = True
                    elif choice == "0":
                        print("Гру завершено.")
                        return
                    else:
                        print("Обери пункт від 0 до 5.")
                except (EOFError, KeyboardInterrupt):
                    print("\nГру завершено.")
                    return
                except Exception as error:
                    print(f"Помилка меню: {error}")

            if player.gold >= 10000:
                print("\nПЕРЕМОГА! Ти став Великим алхіміком!")
                print(f"Зароблено золота: {player.gold}")
                return

        print("\nПОРАЗКА! Минуло 30 днів, а ціль не досягнута.")
        print(f"Ти накопичив {player.gold} із 10000 золотих.")
        print("Спробуй ще раз і краще плануй створення зіль.")
    except Exception as error:
        print(f"Критична помилка гри: {error}")
    finally:
        print("\nДякуємо за гру!")


if __name__ == "__main__":
    main()
