"""Игра угадай число
Компьютер сам загадывает и сам угадывает число.
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Адаптивное угадывание числа

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    low = 1
    high = 100

    while True:
        count += 1
        predict_number = np.random.randint(low, high + 1)  # Предполагаемое число
        if predict_number == number:
            break  # выход из цикла, если угадали
        elif predict_number < number:
            low = predict_number + 1  # Смещение нижней границы поиска
        else:
            high = predict_number - 1  # Смещение верхней границы поиска

    return count


def score_game(predict_function) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        predict_function ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=1000)  # загадали список чисел

    for number in random_array:
        count_ls.append(predict_function(number))

    score = int(np.mean(count_ls))  # находим среднее количество попыток
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == "__main__":
    score_game(random_predict)
