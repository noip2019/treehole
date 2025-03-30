from flask import g
import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name

    def connect(self):
        if 'db' not in g:
            g.db = sqlite3.connect(self.db_name)
            g.db.execute("PRAGMA foreign_keys = 1")
        return g.db

    def register_user(self, user_id, password):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute('INSERT INTO user (id, pd) VALUES (?, ?)', (user_id, password))
        db.commit()

    def delete_user(self, user_id):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute('DELETE FROM user WHERE id = ?', (user_id,))
        db.commit()

    def update_user_password(self, user_id, new_password):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute('UPDATE user SET pd = ? WHERE id = ?', (new_password, user_id))
        db.commit()

    def add_post(self, post_id, time, content, user_id):
        db = self.connect()
        cursor = db.cursor()

        cursor.execute('INSERT INTO post (id, time, content, uid) VALUES (?, ?, ?, ?)', (post_id, time, content, user_id))
        db.commit()

    def delete_post(self, post_id):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute('DELETE FROM post WHERE id = ?', (post_id,))
        db.commit()

    def update_post(self, post_id, new_content):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute('UPDATE post SET content = ? WHERE id = ?', (new_content, post_id))
        db.commit()

    def add_comment(self, comment_id, time, content, post_id, user_id):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute('INSERT INTO comment (id, time, content, belong, uid) VALUES (?, ?, ?, ?, ?)', (comment_id, time, content, post_id, user_id))
        db.commit()

    def delete_comment(self, comment_id):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute('DELETE FROM comment WHERE id = ?', (comment_id,))
        db.commit()

    def update_comment(self, comment_id, new_content):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute('UPDATE comment SET content = ? WHERE id = ?', (new_content, comment_id))
        db.commit()

    def add_favorite_post(self, post_id, user_id):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute('INSERT INTO favorite_post (pid, uid) VALUES (?, ?)', (post_id, user_id))
        db.commit()

    def delete_favorite_post(self, post_id, user_id):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute('DELETE FROM favorite_post WHERE pid = ? AND uid = ?', (post_id, user_id))
        db.commit()

    def show_all_table(self):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        result = {}
        for table in tables:
            cursor.execute(f'SELECT * FROM {table[0]}')
            result[table[0]] = cursor.fetchall()
        return result

    def post_of_user(self, user_id):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM post WHERE uid = ?', (user_id,))
        return cursor.fetchall()
    def post_of_all(self):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM post')
        return cursor.fetchall()
    def get_password(self, user_id):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute('SELECT pd FROM user WHERE id = ?', (user_id,))
        result = cursor.fetchone()
        if result:
            return result[0]
        return None
    def close(self):
        db = g.pop('db', None)
        if db is not None:
            db.close()