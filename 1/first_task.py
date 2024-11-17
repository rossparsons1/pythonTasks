def starts_with_vowel(word):
    vowels = 'aeiou'
    return word[0] in vowels

with open("data/first_task.txt", encoding="utf-8") as file:
    lines = file.readlines()
    words = []

    for line in lines:
        _line = (lines[0]
                 .replace(".", "")
                 .replace("!", "")
                 .replace("?", "")
                 .replace("'", "")
                 .replace("-", " ")
                 .lower().strip()
                 )
        words += _line.split(" ")

    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    word_count = len(words)

    word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    vowel_count = sum(1 for word in words if starts_with_vowel(word))

    vowel_ratio = (vowel_count / word_count) * 100 if word_count > 0 else 0

    print(f'Уникальные слова: {word_freq}')
    print(f'Количество слов, начинающихся на гласную букву: {vowel_count}')
    print(f'Доля слов, начинающихся на гласную букву: {vowel_ratio:.2f}%')

    with open("data/first_task_out.txt", 'w', encoding='utf-8') as out_file:
        for word, freq in word_freq:
            out_file.write(f'{word}:{freq}\n')