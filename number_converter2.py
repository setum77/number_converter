"""
Утилита перевода числа в основные системы счисления
"""

def main():
    while True:
        print("\n" + "="*50)
        print("Выберите систему счисления исходного числа:")
        print("1. Двоичное")
        print("2. Десятичное")
        print("3. Восьмеричное")
        print("4. Шестнадцатеричное")
        print("Для выхода введите 'exit'")
        
        choice = input("\nВведите номер (1-4): ").strip()

        if choice.lower() == 'exit':
            print("Выход из программы.")
            break

        number = input("Введите число: ").strip()
        
        try:
            if choice == '1':
                # Двоичное -> остальные
                decimal = int(number, 2)
                hex_val = hex(decimal)[2:].upper()
                octal_val = oct(decimal)[2:]
                binary = number
            elif choice == '2':
                # Десятичное -> остальные
                decimal = int(number)
                binary = bin(decimal)[2:]
                hex_val = hex(decimal)[2:].upper()
                octal_val = oct(decimal)[2:]
            elif choice == '3':
                # Восьмеричное -> остальные
                decimal = int(number, 8)
                binary = bin(decimal)[2:]
                hex_val = hex(decimal)[2:].upper()
                octal_val = number
            elif choice == '4':
                # Шестнадцатеричное -> остальные
                decimal = int(number, 16)
                binary = bin(decimal)[2:]
                hex_val = number.upper()
                octal_val = oct(decimal)[2:]
            else:
                print("Неверный выбор системы счисления")
                return
            
            # Разбивка двоичного числа на регистры по 16 бит
            if len(binary) > 16:
                chunks = [binary[i:i+16] for i in range(0, len(binary), 16)]
                binary_formatted = ' '.join(chunks)
            else:
                binary_formatted = binary

            # Вывод результатов
            print("\n" + "="*50)
            print(f"Результаты преобразования числа {number}:")
            print("="*50)
            print(f"⚁ - Двоичное (bin): {binary_formatted}")
            print(f"🔟 - Десятичное (dec): {decimal}")
            print(f"⚃ - Восьмеричное (oct) 0o: {octal_val}")
            print(f"⚅ - Шестнадцатеричное (hex) 0X: {hex_val}")

        except ValueError as e:
            print("Ошибка ввода: убедитесь в корректности числа для выбранной системы счисления")

if __name__ == "__main__":
    main()