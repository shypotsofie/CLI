class EngUkrDictionary:
    def __init__(self):
        self.dictionary = {}
    def add_translation(self, eng_word, ukr_word):
        eng_word = eng_word.lower()  # Переведення слова в нижній регістр
        ukr_word = ukr_word.lower()
        if eng_word not in self.dictionary:
            self.dictionary[eng_word] = []  # Якщо слова немає, створюємо порожній список
        if ukr_word not in self.dictionary[eng_word]:
            self.dictionary[eng_word].append(ukr_word)  # Додаємо переклад, якщо його ще немає
    def get_translations(self, eng_word):
        eng_word = eng_word.lower()
        if eng_word in self.dictionary:
            return self.dictionary[eng_word]
        else:
            return f"Слово '{eng_word}' не знайдено у словнику."
    def display_all(self):
        """
        Виводить весь словник.
        """
        if not self.dictionary:
            print("Словник порожній.")
        else:
            print("Англо-український словник:")
            for eng_word, translations in self.dictionary.items():
                print(f"{eng_word}: {', '.join(translations)}")

def main():
    """
    Основна функція для взаємодії з користувачем.
    """
    my_dict = EngUkrDictionary()
    while True:
        print("\n--- Англо-український словник ---")
        print("1. Додати переклад")
        print("2. Отримати переклад слова")
        print("3. Вивести весь словник")
        print("4. Вийти")
        choice = input("Виберіть дію (1-4): ")
        if choice == "1":
            eng_word = input("Введіть англійське слово: ")
            ukr_word = input("Введіть український переклад: ")
            my_dict.add_translation(eng_word, ukr_word)
            print(f"Переклад '{ukr_word}' для слова '{eng_word}' додано.")
        elif choice == "2":
            eng_word = input("Введіть англійське слово для перекладу: ")
            translations = my_dict.get_translations(eng_word)
            if isinstance(translations, list):
                print(f"Переклади для слова '{eng_word}': {', '.join(translations)}")
            else:
                print(translations)
        elif choice == "3":
            my_dict.display_all()
        elif choice == "4":
            print("До побачення!")
            break
        else:
            print("Неправильний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()
