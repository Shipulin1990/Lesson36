def personal_sum(numbers):
    """
    Функция вычисляет сумму всех чисел в коллекции
    """
    result, incorrect_data = 0, 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы - {i}')
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    """
    Функция вычисляет среднее арифметическое чисел в коллекции
    """
    result = None
    try:
        sum_ = personal_sum(numbers)
        result = sum_[0] / (len(numbers) - sum_[1])
    except ZeroDivisionError:
        result = 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
    return result


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
