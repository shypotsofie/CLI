def calculate_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)
def main():
    print("Програма для обчислення середнього арифметичного.")
    user_input = input("Введіть числа через пробіл: ")
    try:
        numbers = list(map(float, user_input.split()))
        if not numbers:
            print("Ви не ввели жодного числа.")
            return
        average_value = calculate_average(numbers)
        print("Середнє значення:", average_value)
    except ValueError:
        print("Помилка: введіть лише числові значення, розділені пробілами.")

if __name__ == "__main__":
    main()
