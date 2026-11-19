import math
import os

# Имена файлов
input_filename = "1_lab_input.txt"
output_filename = "1_lab_output.txt"

# ==========================================
# 0. СОЗДАНИЕ ВХОДНОГО ФАЙЛА (если его нет)
# ==========================================
if not os.path.exists(input_filename):
    with open(input_filename, "w", encoding="utf-8") as f:
        f.write("30\n")  # Записываем тестовый угол альфа
    print(f"Создан файл с тестовыми данными: {input_filename}")

try:
    # ==========================================
    # 1. ЧТЕНИЕ ДАННЫХ ИЗ ФАЙЛА
    # ==========================================
    with open(input_filename, "r", encoding="utf-8") as f_in:
        line = f_in.readline()
        if not line:
            raise ValueError("Файл ввода пуст!")
        alpha_deg = float(line.strip())

    # 2. Переводим градусы в радианы
    alpha = math.radians(alpha_deg)

    # 3. Вычисление по первой формуле
    numerator = math.sin(2 * alpha) + math.sin(5 * alpha) - math.sin(3 * alpha)
    denominator = math.cos(alpha) + 1 - 2 * (math.sin(2 * alpha) ** 2)

    # ==========================================
    # 4. ЗАПИСЬ РЕЗУЛЬТАТОВ В ФАЙЛ
    # ==========================================
    with open(output_filename, "w", encoding="utf-8") as f_out:
        f_out.write(f"Входные данные: угол альфа = {alpha_deg} градусов\n")
        f_out.write("-" * 40 + "\n")

        if abs(denominator) < 1e-9:
            f_out.write("Результат z1: Ошибка! Деление на ноль (угол вне ОДЗ).\n")
            z1 = None
        else:
            z1 = numerator / denominator
            f_out.write(f"Результат z1 = {z1:.6f}\n")

        z2 = 2 * math.sin(alpha)
        f_out.write(f"Результат z2 = {z2:.6f}\n")

        if z1 is not None:
            if math.isclose(z1, z2, abs_tol=1e-5):
                f_out.write("Результаты совпадают!\n")
            else:
                f_out.write("Результаты не совпадают!\n")

    print(f"Лабораторная №1 выполнена. Результаты в файле: {output_filename}")

except Exception as e:
    print(f"Ошибка: {e}")