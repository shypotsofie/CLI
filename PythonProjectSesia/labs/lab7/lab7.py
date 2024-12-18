try:
    zavdana = int(input("Номер завдання: "))

    if zavdana == 1:
        import numpy as np
        import matplotlib.pyplot as plt

        def y_function(x):
            return  5 * np.sin(1/x) * np.cos((x**2 + 1/x)**2)

        # Створення даних
        x = np.linspace(1.01, 4, 100)
        y = y_function(x)

        # Побудова графіка
        plt.figure(figsize=(9, 7))
        plt.plot(x, y)
        plt.xlabel("$x$")
        plt.ylabel("$Y(x)$")
        plt.grid(True)
        plt.legend()
        plt.savefig("graph.png")  # Збереження графіка у файл
        plt.show()

    elif zavdana == 2:
        import matplotlib.pyplot as plt

        def letter_histogram(text, filename="letter.png"):
            # Підрахунок частоти літер
            letter_counts = {}
            for letter in text.lower():
                if letter.isalpha():
                    letter_counts[letter] = letter_counts.get(letter, 0) + 1

            # Візуалізація
            plt.figure(figsize=(10, 6))
            plt.bar(letter_counts.keys(), letter_counts.values())
            plt.xlabel('Літера')
            plt.ylabel('Частота')
            plt.title('Частота появи літер')
            plt.savefig(filename)
            plt.show()

        # Приклад використання:
        text = "Це приклад тексту для аналізу частоти літер."
        letter_histogram(text)

    elif zavdana == 3:
        import matplotlib.pyplot as plt
        import re

        # Текст для аналізу
        text = """
        звичайне речення. питальне? окличне! з трикрапкою... питальне? питальне? питальне? з трикрапкою... з трикрапкою...
        """

        # Розділення тексту на речення
        sentences = re.split(r'(?<=[.!?])\s+', text.strip())
        types = {"звичайні": 0, "питальні": 0, "окличні": 0, "з трикрапкою": 0}

        # Аналіз типів речень
        for sentence in sentences:
            if "..." in sentence:
                types["з трикрапкою"] += 1
            elif sentence.endswith("?"):
                types["питальні"] += 1
            elif sentence.endswith("!"):
                types["окличні"] += 1
            else:
                types["звичайні"] += 1

        # Дані для гістограми
        categories = list(types.keys())
        frequencies = list(types.values())

        # Побудова гістограми
        plt.bar(categories, frequencies)
        plt.title("Частота типів речень у тексті")
        plt.xlabel("Типи речень")
        plt.ylabel("Кількість")
        plt.savefig("sentence_types_fixed.png")  # Збереження графіка
        plt.show()

    else:
        print("Введіть число лише від 1 до 3")

except ValueError:
    print("Ви ввели не числове значення")