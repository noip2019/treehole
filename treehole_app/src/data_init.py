import sqlite3

# 连接到数据库（如果数据库不存在，则会自动创建）
conn = sqlite3.connect('data.db')
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()

# 检查表是否存在的函数
def table_exists(table_name):
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';")
    return cursor.fetchone() is not None

# 创建 user 表并插入初始数据（仅在表不存在时）
if not table_exists('user'):
    cursor.execute('''
    CREATE TABLE user(
        id TEXT PRIMARY KEY,
        pd TEXT
    );
    ''')
    cursor.executemany('INSERT INTO user (id, pd) VALUES (?, ?)', [
        ('user1', 'password1'),
        ('user2', 'password2')
    ])

# 创建 post 表并插入初始数据（仅在表不存在时）
if not table_exists('post'):
    cursor.execute('''
    CREATE TABLE post(
        id TEXT PRIMARY KEY,
        time TEXT,
        content TEXT,
        uid TEXT REFERENCES user(id) ON UPDATE CASCADE
    );
    ''')
    cursor.executemany('INSERT INTO post (id, time, content, uid) VALUES (?, ?, ?, ?)', [
        ('post1', '2023-10-01 12:00:00', 'This is the first post','user1'),
        ('post2', '2023-10-02 13:00:00', 'This is the second post','user2'),
    ])

# 创建 comment 表并插入初始数据（仅在表不存在时）
if not table_exists('comment'):
    cursor.execute('''
    CREATE TABLE comment(
        id TEXT PRIMARY KEY,
        time TEXT,
        content TEXT,
        belong TEXT REFERENCES post(id) ON UPDATE CASCADE,
        uid TEXT REFERENCES user(id) ON UPDATE CASCADE
    );
    ''')
    cursor.executemany('INSERT INTO comment (id, time, content, belong, uid) VALUES (?, ?, ?, ?, ?)', [
        ('comment1', '2023-10-01 12:30:00', 'Great post!','post1', 'user2'),
        ('comment2', '2023-10-02 13:30:00', 'Nice content!','post2', 'user1'),
    ])

# 创建 favorite_post 表（无需初始化数据）
if not table_exists('favorite_post'):
    cursor.execute('''
    CREATE TABLE favorite_post(
        pid TEXT REFERENCES post(id) ON UPDATE CASCADE,
        uid TEXT REFERENCES user(id) ON UPDATE CASCADE,
        PRIMARY KEY(pid, uid)
    );
    ''')
    cursor.executemany('INSERT INTO favorite_post (pid, uid) VALUES (?, ?)', [
        ('post1', 'user2'),
        ('post2', 'user1'),
    ])

# 提交事务
conn.commit()

# 关闭连接
conn.close()