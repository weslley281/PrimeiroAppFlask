from config import mysql

class UserModel:
    @staticmethod
    def get_all_users():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fechall()
        cursor.close()
        return users
    
    @staticmethod
    def get_user_by_id(user_id):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        cursor.close()
        return user
    
    @staticmethod
    def create_user(name, email):
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        mysql.connection.commit()
        cursor.close()
        
    @staticmethod
    def update_user(user_id, name, email):
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (name, email, user_id))
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def delete_user(user_id):
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        mysql.connection.commit()
        cursor.close()