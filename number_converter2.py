"""
Утилита перевода числа в основные системы счисления
"""

def to_twos_complement(value, bits):
    """Преобразует число в дополнительный код с заданным количеством бит"""
    if value < 0:
        value = (1 << bits) + value
    return bin(value)[2:].zfill(bits)

def main():
    first_run = True
    
    while True:
        if first_run:
            print("\n" + "="*50)
            print("Выберите систему счисления исходного числа:")
            print("1. Двоичное (B) - тут и далее, префикс для GX Works3")
            print("2. Десятичное (K)")
            print("3. Восьмеричное (O)")
            print("4. Шестнадцатеричное (H)")
            print("Для выхода введите 'exit'")
            first_run = False
        
        print("\n" + "="*50)
        choice = input("\nВведите номер (1-4) системы счисления: ").strip()

        if choice.lower() == 'exit':
            print("Выход из программы.")
            break

        number = input("Введите число: ").strip()
        # Удаляем возможные пробелы
        number = number.replace(' ', '')
        
        try:
            if choice == '1':
                # Двоичное -> остальные
                # Проверяем количество бит и знак для двоичного числа
                if len(number) % 16 == 0:
                    # Если кратно 16 битам, проверяем знак
                    decimal = int(number, 2)
                    if number[0] == '1':  # Если первый бит = 1, это отрицательное число
                        bits = len(number)
                        decimal = decimal - (1 << bits)
                else:
                    decimal = int(number, 2)
                
                hex_val = hex(decimal & 0xFFFFFFFF)[2:].upper()
                octal_val = oct(decimal & 0xFFFFFFFF)[2:]
                binary = number
            elif choice == '2':
                # Десятичное -> остальные
                decimal = int(number)
                binary = bin(decimal & 0xFFFFFFFF)[2:]
                hex_val = hex(decimal & 0xFFFFFFFF)[2:].upper()
                octal_val = oct(decimal & 0xFFFFFFFF)[2:]
            elif choice == '3':
                # Восьмеричное -> остальные
                decimal = int(number, 8)
                binary = bin(decimal & 0xFFFFFFFF)[2:]
                hex_val = hex(decimal & 0xFFFFFFFF)[2:].upper()
                octal_val = number
            elif choice == '4':
                # Шестнадцатеричное -> остальные
                decimal = int(number, 16)
                binary = bin(decimal & 0xFFFFFFFF)[2:]
                hex_val = number.upper()
                octal_val = oct(decimal & 0xFFFFFFFF)[2:]
            else:
                print("Неверный выбор системы счисления")
                continue
            
            # Определяем формат вывода (16 или 32 бита)
            if -32768 <= decimal <= 65535:
                bits = 16
            else:
                bits = 32
            
            # Формируем двоичное представление в слове/двойном слове
            binary_word = to_twos_complement(decimal, bits)
            
            # Разбивка двоичного числа на регистры по 8 бит
            if len(binary) > 8:
                # Дополняем нулями слева до длины, кратной 8
                padding = (8 - len(binary) % 8) % 8
                padded_binary = '0' * padding + binary
                # Разбиваем на 8-битные группы справа налево
                chunks = [padded_binary[i:i+8] for i in range(0, len(padded_binary), 8)]
                binary_formatted = ' '.join(chunks)
            else:
                binary_formatted = binary
            
            # Разбивка двоичного слова на регистры по 8 бит
            binary_word_formatted = ' '.join([binary_word[i:i+8] for i in range(0, len(binary_word), 8)])

            # Вывод результатов
            
            print(f"\nРезультаты преобразования числа {number}:\n")
            print(f"⚁ - Двоичное (bin) Ob: {binary_formatted}")
            print(f"⚁ - Двоичное слово (D) - {bits} бит: {binary_word_formatted}")
            print(f"🔟 - Десятичное (dec): {decimal}")
            print(f"⚃ - Восьмеричное (oct) 0o: {octal_val}")
            print(f"⚅ - Шестнадцатеричное (hex) 0X: {hex_val}")

        except ValueError as e:
            print("Ошибка ввода: убедитесь в корректности числа для выбранной системы счисления")

if __name__ == "__main__":
    main()