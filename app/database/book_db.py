from database.db_connection import get_connection


class Book_db:
    def create_book(self, data: dict):
        conn = get_connection()
        cur = conn.cursor()

        sql_command = (
            "INSERT INTO Books (`title`, `author`,`genre`) VALUES (%s, %s, %s)"
        )
        values = tuple(data.values())
        print(values)
        cur.execute(sql_command, values)

        new_id = cur.lastrowid
        conn.commit()

        cur.close()
        conn.close()

        return new_id

    def get_all_books(self):
        conn = get_connection()
        cur = conn.cursor(dictionary=True)

        sql_command = "SELECT * FROM `Books`"
        cur.execute(sql_command)

        data = cur.fetchall()

        cur.close()
        conn.close()

        return data

    def get_book_by_id(self, id):

        conn = get_connection()
        cur = conn.cursor(dictionary=True)

        sql_command = "SELECT * FROM `Books` WHERE `id` = %s"
        cur.execute(sql_command, (str(id),))

        data = cur.fetchall()

        cur.close()
        conn.close()

        return data

    def count_total_books(self):

        conn = get_connection()
        cur = conn.cursor(dictionary=True)

        sql_command = "SELECT COUNT(*) FROM `Books`"
        cur.execute(sql_command)

        data = cur.fetchone()

        cur.close()
        conn.close()

        return data

    def count_available_books(self):

        conn = get_connection()
        cur = conn.cursor(dictionary=True)

        sql_command = (
            "SELECT COUNT(*) AS `is_available` FROM `Books` WHERE `is_available`=True"
        )
        cur.execute(sql_command)

        data = cur.fetchall()

        cur.close()
        conn.close()

        return data["`is_available`"]

    def count_borrowed_books(self):

        conn = get_connection()
        cur = conn.cursor(dictionary=True)

        sql_command = "SELECT COUNT(*) AS `is_not_available` FROM `Books` WHERE `is_available`= False"
        cur.execute(sql_command)

        data = cur.fetchall()

        cur.close()
        conn.close()

        return data["`is_not_available`"]

    def count_by_genre(self, genre):

        conn = get_connection()
        cur = conn.cursor(dictionary=True)

        sql_command = "SELECT COUNT(*) AS %s FROM `Books` WHERE `genre`= %s,"
        cur.execute(sql_command, (genre, genre,))

        data = cur.fetchall()

        cur.close()
        conn.close()

        return data[genre]

    def count_active_borrows_by_member(self, member_id):

        conn = get_connection()
        cur = conn.cursor(dictionary=True)

        sql_command = (
            "SELECT COUNT(*) AS `active_borrows` FROM `Books` WHERE `borrowed_by_member_id`= %s"
        )

        cur.execute(sql_command, (member_id,))
        result = cur.fetchone()

        cur.close()
        conn.close()

        return result

    def set_available(self, id, value, member_id):

        conn = get_connection()
        cur = conn.cursor(dictionary=True)

        sql_command = (
            "UPDATE `Books` SET is_available = %s,"
            "borrowed_by_member_id = %s WHERE id = %s"
        )
        sql_values = (value, member_id, id)
        print(sql_command)
        print(sql_values)

        cur.execute(sql_command, (sql_values))

        result = cur.rowcount

        conn.commit()

        cur.close()
        conn.close()

        return result

    def update_book(self, id, data):

        conn = get_connection()
        cur = conn.cursor(dictionary=True)

        values = []
        sql_string = []

        for key, val in data.items():
            sql_string.append(str(key).lower() + " = %s")
            values.append(val)

        values.append(id)
        sql_string = ",".join(sql_string)
        sql_excecute_str = "UPDATE `Books` SET " + sql_string + " WHERE ID = %s"
        sql_values = tuple(values)

        cur.execute(sql_excecute_str, sql_values)
        result = cur.rowcount

        cur.close()
        conn.commit()

        return result


booki = Book_db()
