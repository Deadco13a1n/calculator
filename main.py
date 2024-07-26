from calc import add, subtract, multiply, divide

def main():
    while True:
        print("\nОберіть дію:")
        print("Введіть 'add' щоб додати два числа")
        print("Введіть 'subtract' щоб відняти два числа")
        print("Введіть 'multiply' щоб помножити два числа")
        print("Введіть 'divide' щоб поділіти два числа")
        print("Введіть 'quit' щоб закрити програму")

        user_choice = input(": ")

        if user_choice == "quit":
            break
        elif user_choice in ("add", "subtract", "multiply", "divide"):
            try:
                num1 = float(input("Введіть перше число: "))
                num2 = float(input("Введіть друге число: "))
            except ValueError:
                print("Ви ввели некоректне значення!")
                continue

            if user_choice == "add":
                print(f"Ваш результат: {add(num1, num2)}")
            elif user_choice == "subtract":
                print(f"Ваш результат: {subtract(num1, num2)}") 
            elif user_choice == "multiply":
                print(f"Ваш результат: {multiply(num1, num2)}")
            elif user_choice == "divide":
                try:
                    print(f"Ваш результат: {divide(num1, num2)}")
                except ValueError as e:
                    print(e)

if __name__ == "__main__":
    main()