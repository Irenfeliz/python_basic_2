import random

answers = ['Бесспорно',
           'Мне кажется - да',
           'Пока неясно, попробуй снова',
           'Даже не думай',
           'Предрешено',
           'Вероятнее всего',
           'Спроси позже',
           'Мой ответ - нет',
           'Никаких сомнений',
           'Хорошие перспективы',
           'Лучше не рассказывать',
           'По моим данным - нет',
           'Определённо да',
           'Знаки говорят - да',
           'Сейчас нельзя предсказать',
           'Перспективы не очень хорошие',
           'Можешь быть уверен в этом',
           'Да',
           'Сконцентрируйся и спроси опять',
           'Весьма сомнительно']

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
print('Как тебя зовут?')
name = input()
print('Привет,', name)

flag = True
while flag == True:
    print('Задай свой вопрос,', name)
    question = input()
    print(random.choice(answers))
    print('Хочешь спросить еще о чем-нибудь? да / нет')
    yes_or_no = input()
    if yes_or_no.lower() == 'да':
        flag = True
    else:
        print('Возвращайся если возникнут вопросы!')
        flag = False