import mysql.connector
from logs.set_logger import logging


def get_connection():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port="3306",
        user="root",
        password="1234",
        database="library_db",
    )
    if conn.is_connected:
        logging.info("connection to DB : seccssfull")
        return conn
    else:
        logging.ERROR("the conection to the db has filed")
        return False


def set_tables():
    conn = get_connection()
    if conn.is_connected:
        cur = conn.cursor()
        print("ok")
        cur.execute("""
        CREATE TABLE IF NOT EXISTS `Books`(`id` INT PRIMARY KEY AUTO_INCREMENT,`title` VARCHAR(50) NOT NULL, `author` VARCHAR(50) NOT NULL, `genre` ENUM('Fiction', 'Non-Fiction','Science','History', 'Other') NOT NULL,
    is_available BOOLEAN NOT NULL , borrowed_by_member_id INT)
                    """)
        print("ok")
        conn.commit()

        cur.execute("""CREATE TABLE IF NOT EXISTS `members` (`id` INT PRIMARY KEY AUTO_INCREMENT ,`name` VARCHAR(50) NOT NULL, `email` VARCHAR(50) UNIQUE NOT NULL,
`is_active` BOOLEAN NOT NULL, `total_borrows` INT NOT NULL )""")

        conn.commit()
        cur.close()
    else:
        print("the conection is not valid")
        return None
