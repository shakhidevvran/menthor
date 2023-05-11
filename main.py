


import math


def treugolnik(x1, y1, x2, y2, x3, y3):
    # Вычисляем длины сторон треугольника
    a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    b = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    c = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)

    # Вычисляем полупериметр треугольника
    p = (a + b + c) / 2

    # Вычисляем площадь треугольника по формуле Герона
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))

    # Проверяем прямоугольность треугольника по теореме Пифагора
    pryamougolnik = (a ** 2 + b ** 2 == c ** 2) or (b ** 2 + c ** 2 == a ** 2) or (c ** 2 + a ** 2 == b ** 2)

    # Записываем результаты в файлы
    with open("area.txt", "w") as f1:
        f1.write(str(S))

    with open("truefalse.txt", "w") as f2:
        f2.write(str(pryamougolnik))


# treugolnik(0, 0, 0, 0, 1, 3)
#
# def offer(words):
#     words1 = words.split()
#     words_slov = {}
#
#     for word in words1:
#         if word in words_slov:
#             words_slov[word] += 1
#         else:
#             words_slov[word] = 1
#     slovo = max(words_slov, key=words_slov.get)
#     return f'слово которое встречается чаще всего:{slovo}'
#
# words = input('Введите любое предложение на любом языке:')
#
# print(offer(words))


def times(n):
    times = []

    for i in range(n):
        hours, minutes, seconds = map(int, input(f"Введите время {i+1} в формате 'чч мм сс': ").split())
        times.append(f"{hours:}:{minutes:}:{seconds:}")

    sorted_times = sorted(times)
    print("Сортированные временные моменты:")

    for t in sorted_times:
            print(t)


n = int(input("Введите количество моментов времени: "))
times(n)