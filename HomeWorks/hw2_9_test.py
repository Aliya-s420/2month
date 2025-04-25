import sqlite3

DB_NAME = "store_products.db"

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

def create_table(cursor, create_table_sql):
    try:
        cursor.execute(create_table_sql)
        print("Таблица успешно создана.")
    except sqlite3.Error as e:
        print(f"Ошибка при создании таблицы: {e}")

create_categories_table_sql = '''
    CREATE TABLE IF NOT EXISTS categories (
        code TEXT PRIMARY KEY,
        title TEXT
    )
'''

create_stores_table_sql = '''
    CREATE TABLE IF NOT EXISTS stores (
        store_id INTEGER PRIMARY KEY,
        title TEXT
    )
'''

create_products_table_sql = '''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        title TEXT,
        category_code TEXT,
        unit_price FLOAT,
        stock_quantity INTEGER,
        store_id INTEGER,
        FOREIGN KEY (category_code) REFERENCES categories (code),
        FOREIGN KEY (store_id) REFERENCES stores (store_id)
    )
'''

create_table(cursor, create_categories_table_sql)
create_table(cursor, create_stores_table_sql)
create_table(cursor, create_products_table_sql)

cursor.execute("SELECT COUNT(*) FROM categories")
if cursor.fetchone()[0] == 0:
    cursor.executemany("INSERT INTO categories VALUES (?, ?)", [
        ('FD', 'Food products'),
        ('EL', 'Electronics'),
        ('CL', 'Clothes'),
    ])

cursor.execute("SELECT COUNT(*) FROM stores")
if cursor.fetchone()[0] == 0:
    cursor.executemany("INSERT INTO stores VALUES (?, ?)", [
        (1, 'Asia'),
        (2, 'Globus'),
        (3, 'Spar'),
    ])

cursor.execute("SELECT COUNT(*) FROM products")
if cursor.fetchone()[0] == 0:
    cursor.executemany("INSERT INTO products VALUES (?, ?, ?, ?, ?, ?)", [
        (1, 'Chocolate', 'FD', 10.5, 128, 1),
        (2, 'Jeans', 'CL', 120, 55, 2),
        (3, 't-shirt', 'CL', 0.0, 15, 1),
    ])

conn.commit()

def show_store_list(cursor):
    print("\nВы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже, для выхода из программы введите цифру 0:")
    cursor.execute("SELECT store_id, title FROM stores")
    stores = cursor.fetchall()
    for store_id, title in stores:
        print(f"{store_id}. {title}")
    return [store_id for store_id, _ in stores]

def show_products_by_store(cursor, store_id):
    cursor.execute('''
        SELECT p.title, c.title, p.unit_price, p.stock_quantity
        FROM products p
        JOIN categories c ON p.category_code = c.code
        WHERE p.store_id = ?
    ''', (store_id,))
    products = cursor.fetchall()

    if not products:
        print("В выбранном магазине нет продуктов.")
    else:
        for title, category, price, quantity in products:
            print(f"\nНазвание продукта: {title}")
            print(f"Категория: {category}")
            print(f"Цена: {price}")
            print(f"Количество на складе: {quantity}")

while True:
    valid_ids = show_store_list(cursor)
    user_input = input("Введите id магазина: ").strip()

    if user_input == '0':
        print("Выход из программы.")
        break
    elif user_input.isdigit() and int(user_input) in valid_ids:
        show_products_by_store(cursor, int(user_input))
    else:
        print("Некорректный ввод. Попробуйте снова.")

conn.close()