from bs4 import BeautifulSoup
import requests
from googletrans import Translator

translator = Translator()

# Получаем случайное английское слово и его определение
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        english_word = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        return {
            "english_word": english_word,
            "word_definition": word_definition
        }
    except Exception as e:
        print(f"Произошла ошибка при получении слова: {e}")
        return None

# Главная функция игры
def word_game():
    print("Добро пожаловать в игру 'Угадай слово по определению'!")
    while True:
        word_data = get_english_words()
        if not word_data:
            continue  # если ошибка — берём новое слово

        eng_word = word_data["english_word"]
        eng_def = word_data["word_definition"]

        # Переводим определение слова на русский
        try:
            translated_def = translator.translate(eng_def, dest='ru').text
            translated_word = translator.translate(eng_word, dest='ru').text.lower()
        except Exception as e:
            print(f"Ошибка при переводе: {e}")
            continue

        # Печатаем определение на русском и английском
        print(f"\nОпределение: {translated_def} ({eng_def})")

        # Получаем ответ пользователя
        user_guess = input("Какое это слово? (введите по-русски): ").strip().lower()

        if user_guess == translated_word:
            print("Верно! 🎉")
        else:
            print(f"Неверно. Загаданное слово было: {translated_word} (англ. '{eng_word}')")

        # Повтор?
        again = input("\nХотите сыграть ещё раз? (y/n): ").strip().lower()
        if again != 'y':
            print("Спасибо за игру!")
            break

# Запуск игры
word_game()
