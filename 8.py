'''
import pymysql

conn = None
cursor = None

try:
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='1234',
        database='school',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = conn.cursor() # 创建游标
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall() # 获取查询结果

    for row in result:
        print(row) 

except pymysql.Error as e:
    print(f"数据库操作失败: {e}")
except Exception as e:
    print(f"发生未知错误: {e}")

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    print("数据库连接已关闭。")'''

'''conn = None
cursor = None

try:
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='1234',
        database='school2',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = conn.cursor()
    
    sql = "select * from employees where salary between 8000 and 10000;"
    cursor.execute(sql)
    result = cursor.fetchall()
    
    print(f"查询到 {len(result)} 位符合条件的员工：")
    for row in result:
        print(row)

except pymysql.Error as e:
    print(f"数据库操作失败: {e}")
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    print("数据库连接已关闭。")'''


'''#单挑插入，使用execute()方法
conn = None
cursor = None

try:
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='1234',
        database='school',
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = conn.cursor()
    
    sql = "insert into students (name, gender, age,major) values ('张三', '男', 22,'信息科学');"
    cursor.execute(sql)
    conn.commit()
    print(f'插入成功，影响行数：{cursor.rowcount}')
except pymysql.Error as e:
    conn.rollback()
    print(f"数据库操作失败: {e}")
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()'''

'''conn = None
cursor = None
stds=[('孙七','女',23,'计算机科学'),['周八','男',22,'化学工程']]
try:
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='1234',
        database='school',
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = conn.cursor()

    sql = "insert into students (name, gender, age,major) values (%s, %s, %s, %s);"
    cursor.executemany(sql,stds)
    conn.commit()
    print(f'插入成功，影响行数：{cursor.rowcount}')
except pymysql.Error as e:
    conn.rollback()
    print(f"数据库操作失败: {e}")
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()'''


'''conn = None
cursor = None
try:
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='1234',
        database='company',
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = conn.cursor()
    sql = "update employees set salary = 20000 where emp_name = '张三';"#张三的薪水改为20000
    cursor.execute(sql)
    conn.commit()
    print(f'成功，影响行数：{cursor.rowcount}')
except pymysql.Error as e:
    conn.rollback()
    print(f"数据库操作失败: {e}")
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()'''

'''conn = None
cursor = None
try:
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='1234',
        database='company',
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = conn.cursor()
    sql = "DELETE FROM employees WHERE emp_name = '张三';"#删除张三
    cursor.execute(sql)
    conn.commit()
    print(f'成功，影响行数：{cursor.rowcount}')
except pymysql.Error as e:
    conn.rollback()
    print(f"数据库操作失败: {e}")
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()'''

import pymysql

conn = None
cursor = None

try:
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='1234',
        database='school2',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = conn.cursor()

    # 1. 创建 user 表（新增 gender 枚举字段，默认值为男）
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS user (
        id INT PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        gender ENUM('男', '女') DEFAULT '男',
        phone VARCHAR(20)
    );
    """
    cursor.execute(create_table_sql)
    conn.commit()
    print("1. user 表创建成功！")

    # 2. 插入 5 条用户数据（明确指定 gender 的值）
    insert_sql = "INSERT INTO user (id, username, gender, phone) VALUES (%s, %s, %s, %s);"
    data_list = [
        (1, '张三', '男', '13800000001'),
        (2, '李四', '女', '13800000002'),
        (3, '王五', '男', '13800000003'),
        (4, '赵六', '女', '13800000004'),
        (5, '孙七', '男', '13800000005')
    ]
    cursor.executemany(insert_sql, data_list)
    conn.commit()
    print(f"2. 成功插入 {cursor.rowcount} 条初始数据！")

    # 3. 查询所有男性用户（通过 gender 字段精准查询）
    cursor.execute("SELECT * FROM user WHERE gender = '男';")
    male_users = cursor.fetchall()
    print("3. 查询到的男性用户：", male_users)

    # 4. 修改手机号（将 id=1 的用户手机号修改）
    update_sql = "UPDATE user SET phone = '13900000000' WHERE id = 1;"
    cursor.execute(update_sql)
    conn.commit()
    print(f"4. 手机号修改成功，影响行数：{cursor.rowcount}")

    # 5. 删除 id=3 的数据
    delete_sql = "DELETE FROM user WHERE id = 3;"
    cursor.execute(delete_sql)
    conn.commit()
    print(f"5. id=3 的数据删除成功，影响行数：{cursor.rowcount}")

    # 6. 使用事务完成连续插入
    transaction_sql = "INSERT INTO user (id, username, gender, phone) VALUES (%s, %s, %s, %s);"
    transaction_data = [
        (6, '事务用户A', '男', '15000000001'),
        (7, '事务用户B', '女', '15000000002')
    ]
    cursor.executemany(transaction_sql, transaction_data)
    conn.commit()
    print(f"6. 事务提交成功！共插入 {cursor.rowcount} 条数据。")

except Exception as e:
    if conn:
        conn.rollback()
    print(f"操作失败，已回滚。错误信息：{e}")

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    print("数据库连接已关闭。")