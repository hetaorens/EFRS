import sqlite3

# 连接到SQLite数据库
conn = sqlite3.connect('name_index.db')

# 创建文件索引表
conn.execute('''
    CREATE TABLE IF NOT EXISTS name_index (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_name TEXT NOT NULL,
        file_index TEXT NOT NULL
    )
''')

def save_file_index(file_name, file_index):
    # 插入文件索引记录
    conn.execute('INSERT INTO name_index (file_name, file_index) VALUES (?, ?)', (file_name, file_index))
    conn.commit()

def get_file_index(file_name):
    # 查询文件索引
    cursor = conn.execute('SELECT file_index FROM name_index WHERE file_name = ?', (file_name,))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None

def get_file_index_re(file_name):
    cursor = conn.execute('SELECT file_name, file_index FROM name_index WHERE file_name LIKE ?', ('%' + file_name + '%',))
    results = cursor.fetchall()
    if results:
        return [result for result in results]
    else:
        return []

# 示例用法
# file_name = 'example.txt'
# file_index = '123456'

# # 保存文件索引
# # save_file_index(file_name, file_index)

# # 获取文件索引
# # retrieved_file_index = get_file_index(file_name)
# # print(retrieved_file_index)

# # file_name = 'exampl'
# # retrieved_file_indexes = get_file_index_re(file_name)
# # print(retrieved_file_indexes)


# import hashlib
# for i in range(10):
#     save_file_index(str(i)+"A", hashlib.sha1(str(i).encode()).hexdigest())

# file_name = '1'
# retrieved_file_indexes = get_file_index_re(file_name)
# print(retrieved_file_indexes)
# 关闭数据库连接
conn.close()
