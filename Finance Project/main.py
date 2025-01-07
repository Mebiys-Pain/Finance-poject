from db import create_db, add_transaction, get_balance, get_transactions

def main_menu():
    print("\nДобро пожаловать в приложение Finance Tracker!")
    print("Выберите действие:")
    print("1. Добавить доход/расход")
    print("2. Просмотреть баланс")
    print("3. Просмотреть историю транзакций")
    print("4. Выйти")

def add_transaction_menu():
    print("\nДобавление транзакции")
    category = input("Введите категорию (например, 'Еда', 'Зарплата', 'Развлечения'): ")
    amount = float(input("Введите сумму (используйте знак '-' для расходов): "))
    add_transaction(category, amount)
    print("Транзакция успешно добавлена!")

def show_balance():
    balance = get_balance()
    print(f"\nВаш текущий баланс: {balance:.2f} рублей")

def show_transactions():
    transactions = get_transactions()
    if not transactions:
        print("\nИстория транзакций пуста.")
        return

    print("\nИстория транзакций:")
    print("{:<10} {:<20} {:<10}".format("Дата", "Категория", "Сумма"))
    print("-" * 40)
    for t in transactions:
        print("{:<10} {:<20} {:<10.2f}".format(t[0], t[1], t[2]))

if __name__ == "__main__":
    create_db()  # Создаем базу данных, если ее еще нет

    while True:
        main_menu()
        choice = input("Ваш выбор: ")

        if choice == "1":
            add_transaction_menu()
        elif choice == "2":
            show_balance()
        elif choice == "3":
            show_transactions()
        elif choice == "4":
            print("Спасибо за использование приложения! До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")