from database.db_connection import get_connection


class Book_db:
    def create_book(self, data: dict):
        conn = get_connection()
        cur = conn.cursor()

        sql_command = (
            "INSERT INTO Books (`title`, `author`,`genre`) VALUES (%s, %s, %s),"
        )
        values = tuple(data.values())
        cur.execute(sql_command, values)

        conn.commit()

        cur.close()
        conn.close()

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

        sql_command = "SELECT * FROM `Books` WHERE `id` = %s,"
        cur.execute(sql_command, id)

        data = cur.fetchone()

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
            "SELECT COUNT(*) AS `is_available` FROM `Books` WHERE "
            "`is_available`=True"
        )
        cur.execute(sql_command)

        data = cur.fetchall()

        cur.close()
        conn.close()

        return data["`is_available`"]

    def count_borrowed_books(self):

        conn = get_connection()
        cur = conn.cursor(dictionary=True)

        sql_command = (
            "SELECT COUNT(*) AS `is_not_available` FROM `Books` WHERE `is_available`= False"
        )
        cur.execute(sql_command)

        data = cur.fetchall()

        cur.close()
        conn.close()

        return data["`is_not_available`"]
    
    def count_by_genre(self, genre):

        conn = get_connection()
        cur = conn.cursor(dictionary=True)

        sql_command = "SELECT COUNT(*) AS %s FROM `Books` WHERE `genre`= %s,"
        cur.execute(sql_command, genre, genre)

        data = cur.fetchall()

        cur.close()
        conn.close()

        return data[genre]

    def count_active_borrows_by_member(self, member_id):

        conn = get_connection()
        cur = conn.cursor(dictionary=True)

        sql_command = "SELECT COUNT(*) AS `active_borrows` FROM `Books`" \
            " WHERE `borrowed_by_member_id`= %s,"

        cur.execute(sql_command, member_id)

    def set_available(self,id, value ,member_id):
        

booki = Book_db()


