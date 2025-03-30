
import sqlite3
class DatabaseManager:
    def __init__(self, db_name):
        """
        初始化数据库连接
        :param db_name: 数据库名称
        """
        self.conn = sqlite3.connect(db_name)
        self.conn.execute("PRAGMA foreign_keys = 1")
        self.cursor = self.conn.cursor()
    def register_user(self,user_id, password):
        """
        注册新用户
        :param user_id: 用户ID
        :param password: 密码
        """
        self.cursor.execute('INSERT INTO user (id, pd) VALUES (?, ?)', (user_id, password))
        self.conn.commit()
    def delete_user(self,user_id):
        """
        删除用户
        :param user_id: 用户ID
        """
        self.cursor.execute('DELETE FROM user WHERE id = ?', (user_id,))
        self.conn.commit()
    def update_user_password(self,user_id, new_password):
        """
        更新用户密码
        :param user_id: 用户ID
        :param new_password: 新密码
        """
        self.cursor.execute('UPDATE user SET pd = ? WHERE id = ?', (new_password, user_id))
        self.conn.commit()
    def add_post(self, post_id, time, content, user_id):
        """
        添加新帖子
        :param post_id: 帖子ID "
        "param time: 时间
        :param content: 内容"
        "param user_id: 用户ID
        """
        self.cursor.execute('INSERT INTO post (id, time, content, uid) VALUES (?, ?, ?, ?)', (post_id, time, content, user_id))
        self.conn.commit()
    def delete_post(self,post_id):
        """
        删除帖子
        :param post_id: 帖子ID
        """
        self.cursor.execute('DELETE FROM post WHERE id = ?', (post_id,))
        self.conn.commit()
    def update_post(self,post_id, new_content):
        """"
        "更新帖子内容
        :param post_id: 帖子ID"
        "param new_content: 新内容
        """
        self.cursor.execute('UPDATE post SET content = ? WHERE id = ?', (new_content, post_id))
        self.conn.commit()
    def add_comment(self, comment_id, time, content, post_id, user_id):
        """
        添加新评论"
        "param comment_id: 评论ID
        "param time: 时间"
        "param content: 内容
        "param post_id: 帖子ID"
        "param user_id: 用户ID
        """
        self.cursor.execute('INSERT INTO comment (id, time, content, belong, uid) VALUES (?, ?, ?, ?, ?)', (comment_id, time, content, post_id, user_id))
        self.conn.commit()
    def delete_comment(self, comment_id):
        """"
        "删除评论
        :param comment_id: 评论ID
        """
        self.cursor.execute('DELETE FROM comment WHERE id = ?', (comment_id,))
        self.conn.commit()
    def update_comment(self, comment_id, new_content):
        """"
        "更新评论内容
        :param comment_id: 评论ID "
        "param new_content: 新内容
        """
        self.cursor.execute('UPDATE comment SET content = ? WHERE id = ?', (new_content, comment_id))
        self.conn.commit()
    def add_favorite_post(self, post_id, user_id):
        """
        添加收藏帖子"
        "param post_id: 帖子ID
        "param user_id: 用户ID
        """
        self.cursor.execute('INSERT INTO favorite_post (pid, uid) VALUES (?, ?)', (post_id, user_id))
        self.conn.commit()
    def delete_favorite_post(self, post_id, user_id):
        """"
        "删除收藏帖子
        :param post_id: 帖子ID"
        "param user_id: 用户ID
        """
        self.cursor.execute('DELETE FROM favorite_post WHERE pid = ? AND uid = ?', (post_id, user_id))
        self.conn.commit()
    def show_all_table(self):
        """
        显示所有表格内容
        """
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = self.cursor.fetchall()
        for table in tables:
            print(table[0])
            self.cursor.execute(f'SELECT * FROM {table[0]}')
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
    def post_of_user(self, user_id):
        """
        获取用户的所有帖子
        :param user_id: 用户ID
        """        
        self.cursor.execute('SELECT * FROM post WHERE uid = ?', (user_id,))
        return self.cursor.fetchall()
    
    def close(self):
        """
        关闭数据库连接
        """
        self.conn.close()
    def __del__(self):
        """
        析构函数，确保关闭数据库连接
        """
        self.close()
if __name__ == "__main__":
    import sys
    sys.path.append('../')
    # 测试代码
    db = DatabaseManager('C:\\Users\\omen\\code\\treehole\\treehole_app\\data.db')

    db.show_all_table()
