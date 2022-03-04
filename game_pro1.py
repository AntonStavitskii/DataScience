"""Игрjа угадай число"""

import numpy as np

number = np.random.randint(1, 101) # загадываем число

def smart_predict(number) -> int:
    """Умно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0
    smart_start = 1
    smart_adge = 101
    while True:
        count += 1
        predict_number = np.random.randint(smart_start, smart_adge) # предполагаемое число
        if predict_number>number:
            smart_adge = predict_number
        elif predict_number<number:
            smart_start = predict_number    
        else:        
            break # выход из цикла, если угадали
    return(count)


def score_game(smart_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(smart_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(smart_predict)

