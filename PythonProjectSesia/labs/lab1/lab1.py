def main():
    """
    Основна функція для запуску вибраного завдання.
    """
    try:
        zavdana = int(input("Номер завдання (1-3): "))
        if zavdana == 1:
            task1()
        elif zavdana == 2:
            task2()
        elif zavdana == 3:
            task3()
        else:
            print("Введіть число лише від 1 до 3.")
    except ValueError:
        print("Ви ввели не числове значення.")

def task1():
    """
    Виконує завдання 1: арифметичні операції.
    """
    a = 2
    b = 5
    c = a + b
    g = a - b
    h = a * b
    l = a / b
    print(c, g, h, l)

def task2():
    """
    Виконує завдання 2: розрахунок сумарної ваги мішків.
    """
    mishki = 10
    first_m = int(input("Введіть вагу у кг для першого мішка: "))
    second_m_kg = int(input("Введіть вагу у кг для другого мішка: "))
    second_m_g = int(input("Введіть вагу у грамах для другого мішка: "))
    other_kg = int(input("Введіть вагу у кг для решти мішків: "))
    other_g = int(input("Введіть вагу у грамах для решти мішків: "))
    sum_of_8_mishkiv = (other_kg * 1000 + other_g) * 8
    first_m_gram = first_m * 1000
    second_m_full_y_gramah = second_m_kg * 1000 + second_m_g
    sum_total_gram = sum_of_8_mishkiv + first_m_gram + second_m_full_y_gramah
    print("Сумарно в грамах: %d" % sum_total_gram)
def task3():
    """
    Виконує завдання 3: розрахунок кількості тістечок, проданих на перерві.
    """
    def cakes_sold_first_break(total_cakes, multiplier):
        cakes_first_break = total_cakes / (7 * multiplier + 1)
        return cakes_first_break
    total_cakes = int(input("Введіть загальну кількість спечених тістечок: "))
    multiplier = int(input("Введіть у скільки разів більше тістечок продали на другій перерві: "))
    result = cakes_sold_first_break(total_cakes, multiplier)
    print(f"На першій перерві продали {result} тістечок.")

if __name__ == "__main__":
    main()
