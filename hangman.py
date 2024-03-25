import random
word_list = [
    "вітер", "дощ", "квітка", "сад", "море",
    "ліс", "гора", "ріка", "дерево", "хмара",
    "зоря", "сонце", "трава", "птах", "дом",
    "вулиця", "міст", "вечір", "ранок", "ніч",
    "сніг", "лист", "фрукт", "овоч", "поле",
    "день", "край", "берег", "світ", "коло",
    "день", "ноч", "тепло", "холод", "зима",
    "літо", "весна", "осінь", "світло", "темно",
    "час", "мир", "знання", "робота", "сім'я",
    "діти", "школа", "учень", "вчитель", "роздум",
    "сила", "слово", "сміх", "природа", "краса",
    "вірш", "книга", "письмо", "мрія", "спогад",
    "сон", "життя", "подорож", "почуття", "душа",
    "відпочинок", "здоров'я", "їжа", "відчуття",
    "світогляд", "мудрість", "дух", "допомога", "мистецтво",
    "творчість", "успіх", "радість", "зрада", "любов",
    "дружба", "рівень", "температура", "натура", "ріст",
    "крок", "красуня", "диво", "радість", "втіха",
    "веселка", "зірка", "магія", "ідея", "розум",
    "відкриття", "фантазія", "виняток", "легенда", "допомога",
    "уява", "гордість", "почуття", "слава", "сподівання",
    "благополуччя", "заспокоєння", "впевненість", "задоволення", "щастя",
    "покій", "мир", "турбота", "добро", "ласка",
    "побажання", "свято", "тривога", "злагода", "тепло",
    "затишок", "щира"]


def get_word():
    return word_list[random.randint(0, len(word_list) - 1)].upper()


def display_human(tries):
    stages = [  # final state: head, body, both hands, both legs
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # head, body, both hands, one leg
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # head, body, both hands
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        # head, body and one hand
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # head and body
        '''
            --------
            |      |
            |      O
            |      |
            |      |
            |     
            -
        ''',
        # head and neck
        '''
           --------
           |      |
           |      O
           |      |
           |      
           |     
           -
        ''',
        # head
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # loop
        '''
            --------
            |      |
            |      
            |    
            |      
            |     
            -
        ''',
        # Initial state
        '''
           --------
           |      
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]


def display_info(word, tries=0, char='_'):
    """Displaying info about stick-man"""
    print(f"Your stick-man looks like:\n{display_human(tries)}.\nTried letters list: {tried_letters}")

    if not char in word or tries != 0:
        print(f"You have {tries} tries left. The word looks like: {''.join(word)}")


def play(word):
    """Main gameplay structure"""
    word_completion = '_' * len(word)  # line, which contain _ for each letter guessed words
    global tried_letters
    tried_letters = []
    guessed_letters = []  # used letters list
    guessed_words = []  # already used words list
    tries = 8

    print("Let's play HANGMAN!")
    display_info(word_completion, tries)

    while True:
        if tries == 0:
            print(f"I'm sorry but you lost\n{display_human(tries)}")
            print(f'The word was: {word}')
            break
        elif '_' not in word_completion:
            print(f'Congratulations! You guessed in  {8 - tries} tries!')
            display_info(word_completion, tries)
            break
        s = input('Enter a word or a letter:\n').upper()

        for i in s:
            if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 !#$%&*+-=?@^_,.'\"":
                print('\nНеверный ввод! Повторите попытку')
                break

        if s in guessed_words or s in guessed_letters:
            print(f"\nLetter '{s}' is already tried!")
            continue
        elif len(s) > 1:
            if s == word:
                print(f'Congratulations! You guessed the word in {8 - tries} tries. Guessed word - {word}')
                break
            else:
                tries -= 1
                guessed_words.append(s)
                print("\nI'm sorry but you guessed wrong!")
                display_info(word_completion, tries)
        else:
            if s in word:
                tried_letters.append(s)
                guessed_letters.append(s)
                word_completion = [s if word[i] == s else word_completion[i] for i in range(len(word))]
                if '_' in word_completion:
                    print('\nCongratulations! You guessed a letter!')
                    display_info(word_completion, tries)
                else:
                    print(f'Congratulations! You guessed the word in {8 - tries} tries. Guessed word - {word}')
                    break
            else:
                tried_letters.append(s)
                tries -= 1
                if tries != 0:
                    print("\nI'm sorry but you guessed wrong!")
                    display_info(word_completion, tries)
    return word


while True:
    used_words = []
    word = get_word()
    while word in used_words:
        word = get_word()
    used_words.append(play(word))
    if input(f'Do you want to try again? (y / n)\n').lower() != 'y':
        print('Good bye!')
        break