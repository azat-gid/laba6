import os

# Имена файлов
input_filename = "4_lab_input.txt"
output_filename = "4_lab_output.txt"

# ==========================================
# 0. СОЗДАНИЕ ВХОДНОГО ФАЙЛА (если его нет)
# ==========================================
if not os.path.exists(input_filename):
    with open(input_filename, "w", encoding="utf-8") as f:
        # Тестовый массив из вашей лабы
        f.write("0 -5 3 2 -1 0 4 -2 0\n")
    print(f"Создан файл с тестовыми данными: {input_filename}")

try:
    # ==========================================
    # 1. ЧТЕНИЕ ДАННЫХ ИЗ ФАЙЛА
    # ==========================================
    with open(input_filename, "r", encoding="utf-8") as f_in:
        content = f_in.read()
        arr = [int(x) for x in content.split()]

    n = len(arr)

    # ==========================================
    # 2. ВЫЧИСЛЕНИЯ
    # ==========================================
    # Пункт 1: Произведение элементов с четными номерами (индексы 1, 3, 5...)
    product_even = 1
    for i in range(1, n, 2):
        product_even *= arr[i]

    # Пункт 2: Сумма между первым и последним нулевыми элементами
    indices_zero = [i for i, x in enumerate(arr) if x == 0]

    if len(indices_zero) >= 2:
        first_zero = indices_zero[0]
        last_zero = indices_zero[-1]
        sum_between = sum(arr[first_zero + 1: last_zero])
        sum_between_str = str(sum_between)
    else:
        sum_between_str = "В массиве меньше двух нулей!"

    # Пункт 3: Преобразование
    positive_part = [x for x in arr if x >= 0]
    negative_part = [x for x in arr if x < 0]
    new_arr = positive_part + negative_part

    # ==========================================
    # 3. ЗАПИСЬ РЕЗУЛЬТАТОВ В ФАЙЛ
    # ==========================================
    with open(output_filename, "w", encoding="utf-8") as f_out:
        f_out.write(f"Исходный массив: {arr}\n")
        f_out.write("-" * 40 + "\n")
        f_out.write(f"1. Произведение элементов с четными номерами: {product_even}\n")
        f_out.write(f"2. Сумма между первым и последним нулем: {sum_between_str}\n")
        f_out.write(f"3. Преобразованный массив: {new_arr}\n")

    print(f"Лабораторная №4 выполнена. Результаты в файле: {output_filename}")

except Exception as e:
    print(f"Ошибка: {e}")