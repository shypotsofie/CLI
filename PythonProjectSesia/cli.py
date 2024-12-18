import os
import sys
import importlib.util

# Шлях до папки з лабораторними роботами
LABS_DIR = "labs"


def list_labs():
    """
    Виводить список усіх доступних лабораторних робіт.
    """
    labs = sorted(os.listdir(LABS_DIR))
    print("Доступні лабораторні роботи:")
    for idx, lab in enumerate(labs, start=1):
        lab_dir = os.path.join(LABS_DIR, lab)
        readme_path = os.path.join(lab_dir, "README.md")

        # Отримати опис із README.md
        if os.path.isdir(lab_dir) and os.path.isfile(readme_path):
            with open(readme_path, "r", encoding="utf-8") as f:
                description = f.readline().strip().replace("#", "").strip()
        else:
            description = "Опис відсутній."

        print(f"{idx}. {lab} - {description}")


def run_lab(lab_number):
    """
    Запускає обрану лабораторну роботу.
    """
    labs = sorted(os.listdir(LABS_DIR))

    try:
        lab_name = labs[lab_number - 1]
        lab_file = os.path.join(LABS_DIR, lab_name, f"{lab_name}.py")

        if not os.path.isfile(lab_file):
            print(f"Файл {lab_name}.py відсутній у папці {lab_name}.")
            return

        # Динамічно імпортуємо модуль
        spec = importlib.util.spec_from_file_location("lab_module", lab_file)
        lab_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(lab_module)

        print(f"Запуск лабораторної роботи {lab_number}...\n")

        # Перевіряємо наявність функції main
        if hasattr(lab_module, "main") and callable(lab_module.main):
            lab_module.main()
        else:
            print(f"Помилка: у модулі {lab_name}.py відсутня функція 'main'.")
    except (IndexError, FileNotFoundError):
        print(f"Лабораторної роботи з номером {lab_number} не знайдено.")
    except Exception as e:
        print(f"Помилка під час виконання лабораторної: {e}")


def print_help():
    """
    Виводить доступні команди.
    """
    print("Доступні команди CLI:")
    print("  list              - Вивести список лабораторних робіт")
    print("  run <lab_number>  - Запустити обрану лабораторну роботу")
    print("  help              - Вивести довідку")


def main():
    if len(sys.argv) < 2:
        print("Будь ласка, введіть команду. Для довідки введіть 'help'.")
        return

    command = sys.argv[1]

    if command == "list":
        list_labs()
    elif command == "run":
        if len(sys.argv) < 3:
            print("Вкажіть номер лабораторної роботи:")
            return
        try:
            lab_number = int(sys.argv[2])
            run_lab(lab_number)
        except ValueError:
            print("Номер лабораторної роботи має бути цілим числом.")
    elif command == "help":
        print_help()
    else:
        print("Невідома команда. Для довідки введіть 'help'.")


if __name__ == "__main__":
    main()

    """
 1. Вивести список лабораторних робіт
```
python cli.py list

2. Запустити лабораторну роботу

python cli.py run <номер_роботи>

Наприклад:

python cli.py run 1

3. Довідка

python cli.py help
 """

