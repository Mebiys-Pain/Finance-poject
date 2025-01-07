# db.py
import sqlite3

DB_NAME = "finance.db"

def create_db():
    """Создает таблицы в базе данных, если их нет."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            type TEXT CHECK(type IN ('income', 'expense')) NOT NULL,
            date TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    conn.commit()
    conn.close()

def add_transaction(amount, category, transaction_type):
    """Добавляет новую транзакцию в базу данных."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO transactions (amount, category, type)
        VALUES (?, ?, ?)
        """,
        (amount, category, transaction_type)
    )

    conn.commit()
    conn.close()

def get_balance():
    """Возвращает текущий баланс (доходы - расходы)."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT SUM(CASE WHEN type = 'income' THEN amount ELSE -amount END) AS balance
        FROM transactions
        """
    )
    balance = cursor.fetchone()[0] or 0.0

    conn.close()
    return balance

def get_transactions():
    """Возвращает список всех транзакций."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, amount, category, type, date
        FROM transactions
        ORDER BY date DESC
        """
    )
    transactions = cursor.fetchall()

    conn.close()
    return transactions

# Создание базы данных при первом запуске
if __name__ == "__main__":
    create_db()
    print("База данных успешно создана.")

# Подсоединение к базе данных

import sqlite3
from datetime import datetime

DB_NAME = "finance_tracker.db"

def create_db():
    """Создает таблицу для транзакций, если она еще не существует."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                category TEXT NOT NULL,
                amount REAL NOT NULL
            )
        """)
        conn.commit()

def add_transaction(category, amount):
    """Добавляет новую транзакцию в базу данных."""
    date = datetime.now().strftime("%Y-%m-%d")  # Текущая дата
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO transactions (date, category, amount)
            VALUES (?, ?, ?)
        """, (date, category, amount))
        conn.commit()

def get_balance():
    """Возвращает текущий баланс (сумму всех доходов и расходов)."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT SUM(amount) FROM transactions
        """)
        result = cursor.fetchone()
        return result[0] if result[0] else 0.0

def get_transactions():
    """Возвращает список всех транзакций."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT date, category, amount FROM transactions
            ORDER BY date DESC
        """)
        return cursor.fetchall()