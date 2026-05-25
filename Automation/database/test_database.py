import sqlite3


def test_create_users_table():

    connection = sqlite3.connect("Automation/database/ecommerce.db")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT,
            password TEXT
        )
    """)

    connection.commit()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")

    table = cursor.fetchone()

    assert table is not None

    connection.close()

def test_insert_user():

    connection = sqlite3.connect("Automation/database/ecommerce.db")

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO users (email, password)
        VALUES (?, ?)
    """, ("qa_test@example.com", "Test123"))

    connection.commit()

    cursor.execute("""
        SELECT * FROM users
        WHERE email='qa_test@example.com'
    """)

    user = cursor.fetchone()

    assert user is not None

    connection.close()

def test_validate_user_email():

    connection = sqlite3.connect("Automation/database/ecommerce.db")

    cursor = connection.cursor()

    cursor.execute("""
        SELECT email
        FROM users
        WHERE email='qa_test@example.com'
    """)

    result = cursor.fetchone()

    assert result[0] == "qa_test@example.com"

    connection.close()