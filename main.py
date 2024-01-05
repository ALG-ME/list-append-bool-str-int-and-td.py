my_list = []

while True:
    user_input = input("Введите элемент (строка, целое число, булево значение, float или 'конец' для завершения): ")

    if user_input.lower() == 'конец':
        break

    if user_input.lower() == 'true':
        my_list.append(True)
    elif user_input.lower() == 'false':
        my_list.append(False)
    else:
        # Попробуем преобразовать введенное значение в разные типы данных
        try:
            # Попытка преобразовать в целое число
            value = int(user_input)
            my_list.append(value)
        except ValueError:
            try:
                # Попытка преобразовать в число с плавающей точкой
                value = float(user_input)
                my_list.append(value)
            except ValueError:
                # Если не удалось преобразовать, добавляем как строку
                my_list.append(str(user_input))

# Выведите окончательный список на экран и количество элементов в нем
print("Окончательный список:", my_list)
print("Количество элементов в списке:", len(my_list))
