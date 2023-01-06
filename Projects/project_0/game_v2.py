"""
Игра "Угадай число".
Компьютер сам загадывает и угадывает число.
"""
import numpy as np


def random_predict(number:int=1) -> int:
    """Функция отгадывает загаданное число,
    последовательно вдвое сокращая диапазон
    возможных вариантов.

    Args:
        number (int, optional): Загаданное число. По умолчанию = 1.

    Returns:
        int: Количество попыток угадывания.
    
    """

    count = 0 # Начальное значение количества попыток.
    predict_number = 50 # Вариант числа - в начале - середина диапазона.
    max_limit = 101 # Максимальное значение диапазона.
    min_limit = 0 # Минимальное значение диапазона.

    while True:
        count += 1
        if number == predict_number:
            break # Выход из цикла, если число угадано.
        elif number > predict_number: 
            min_limit = predict_number
            predict_number += (max_limit-min_limit) // 2
        elif number < predict_number:
            max_limit = predict_number
            predict_number -= (max_limit-min_limit) // 2

    return(count)

def score_game(random_predict) -> int:
    """Функция вычисляет, за какое количество попыток в среднем
    из 1000 подходов алгоритм угадывает число.

    Args:
        random_predict ([type]): Функция угадывания.

    Returns:
        int: Среднее количество попыток.
    
    """

    count_ls = [] # Список для сохранения количества попыток.
    np.random.seed(1) # Фиксируем сид для воспроизводимости.
    random_array = np.random.randint(1, 101, size=(1000)) # Загадываем числа.  

    for number in random_array:
        count_ls.append(random_predict(number)) # Сохраняем кол-во попыток.  

    score = int(np.mean(count_ls)) # Считаем среднее количество попыток.  

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)