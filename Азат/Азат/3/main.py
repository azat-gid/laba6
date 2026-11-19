import itertools
import os


# 1. Столбцы, где есть хотя бы один ноль
def count_zero_cols(m):
    return sum(0 in [m[i][j] for i in range(len(m))] for j in range(len(m[0])))


# 2. Номер строки с самой длинной серией
def longest_series_row(m):
    best_row, max_len = 1, 0
    for i, row in enumerate(m):
        curr_max = max(len(list(g)) for _, g in itertools.groupby(row))
        if curr_max > max_len:
            max_len = curr_max
            best_row = i + 1
    return best_row


# Имена файлов
input_filename = "5_lab_input.txt"
output_filename = "5_lab_output.txt"

# ==========================================
# 0. СОЗДАНИЕ ВХОДНОГО ФАЙЛА (если его нет)
# ==========================================
if not os.path.exists(input_filename):
    with open(input_filename, "w", encoding="utf-8") as f:
        # Тестовая матрица 3x4 (размеры и сама матрица)
        f.write("3 4\n")
        f.write("1 2 3 4\n")
        f.write("5 6 7 8\n")
        f.write("9 0 1 2\n")
    print(f"Создан файл с тестовыми данными: {input_filename}")

try:
    # ==========================================
    # 1. ЧТЕНИЕ ДАННЫХ ИЗ ФАЙЛА
    # ==========================================
    with open(input_filename, "r", encoding="utf-8") as f_in:
        sizes = f_in.readline().split()
        r, c = int(sizes[0]), int(sizes[1])

        matrix = []
        for line in f_in:
            if line.strip():
                row = [int(x) for x in line.split()]
                if len(row) != c:
                    raise ValueError(f"Ожидалось {c} столбцов, получено {len(row)}")
                matrix.append(row)

        if len(matrix) != r:
            raise ValueError(f"Ожидалось {r} строк, получено {len(matrix)}")

    # ==========================================
    # 2. ВЫЧИСЛЕНИЯ
    # ==========================================
    zeros_count = count_zero_cols(matrix)
    best_series_row = longest_series_row(matrix)

    # ==========================================
    # 3. ЗАПИСЬ РЕЗУЛЬТАТОВ В ФАЙЛ
    # ==========================================
    with open(output_filename, "w", encoding="utf-8") as f_out:
        f_out.write("Исходная матрица:\n")
        for row in matrix:
            f_out.write(f"{row}\n")

        f_out.write("\nРезультаты:\n")
        f_out.write(f"1. Столбцов с нулями: {zeros_count}\n")
        f_out.write(f"2. Строка с самой длинной серией: {best_series_row}\n")

    print(f"Лабораторная №5 выполнена. Результаты в файле: {output_filename}")

except Exception as e:
    print(f"Ошибка: {e}")