import random

def task1():
    words1 = ["Amazing", "Incredible", "Beautiful", "Wonderful", "Famous"]
    words2 = ["day", "evening", "moment", "time", "space"]
    words3 = ["is coming", "is approaching", "is starting", "is ending", "is continuing"]

    def generate_phrase():
        first_word = random.choice(words1)
        second_word = random.choice(words2)
        third_word = random.choice(words3)
        return f"{first_word} {second_word} {third_word}"

    random_phrase = generate_phrase()
    print("Згенерована фраза:", random_phrase)

def task2(file=None):
    file_path = "book.txt"
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            characters_with_spaces = len(text)
            characters_without_spaces = len(text.replace(" ", ""))
            print(f"Кількість символів з пробілами: {characters_with_spaces}")
            print(f"Кількість символів без пробілів: {characters_without_spaces}")
    except FileNotFoundError as e:
        print(f"Помилка: файл не знайдено. Шлях: {e.filename}")
    except Exception as e:
        print(f"Сталася непередбачена помилка: {e}")

def task3():
    def sentence_analysis(text):
        sentences = text.split('. ') + text.split('! ') + text.split('? ') + text.split('… ')
        total_sentences = len(sentences)
        exclamatory_sentences = text.count('!')
        question_sentences = text.count('?')
        ellipsis_sentences = text.count('…')
        print("Загальна кількість речень:", total_sentences)
        print("Кількість окличних речень:", exclamatory_sentences)
        print("Кількість питальних речень:", question_sentences)
        print("Кількість речень з трикрапкою:", ellipsis_sentences)

    text = "Привіт! Як справи? Це приклад тексту... Він містить різні типи речень! Ще одне речення?"
    sentence_analysis(text)

def main():
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

if __name__ == "__main__":
    main()