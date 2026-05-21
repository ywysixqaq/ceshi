import pymysql

class DBHelper:
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost', user='root', password='1234',
            database='school2', charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

    def exec(self, sql, params=None):
        try:
            with self.conn.cursor() as cur:
                cur.execute(sql, params)
                self.conn.commit()
                return cur
        except Exception as e:
            self.conn.rollback()
            print(f"Error: {e}")
            return None

    # 新增：专门处理批量插入的方法
    def executemany(self, sql, params=None):
        try:
            with self.conn.cursor() as cur:
                cur.executemany(sql, params)
                self.conn.commit()
                return cur
        except Exception as e:
            self.conn.rollback()
            print(f"Error: {e}")
            return None

    def query(self, sql, params=None):
        try:
            with self.conn.cursor() as cur:
                cur.execute(sql, params)
                return cur.fetchall()
        except Exception as e:
            print(f"Error: {e}")
            return None

class UserManager:
    def __init__(self, db_helper):
        self.db = db_helper
        self.prepare_table()

    def prepare_table(self):
        # 重建表结构
        self.db.exec("DROP TABLE IF EXISTS user;")
        self.db.exec("""
            CREATE TABLE user (
                id INT PRIMARY KEY,
                username VARCHAR(50),
                gender ENUM('男', '女') DEFAULT '男',
                phone VARCHAR(20)
            );
        """)
        # 预置初始数据
        init_data = [
            (1, '张三', '男', '13000000000'),
            (2, '李四', '女', '13100000000'),
            (3, '王五', '男', '13200000000')
        ]
        # 修改：调用新增的 executemany 方法进行批量插入
        self.db.executemany("INSERT INTO user (id, username, gender, phone) VALUES (%s, %s, %s, %s)", init_data)

    def show_all(self, step_name):
        print(f"\n--- {step_name} ---")
        all_users = self.db.query("SELECT * FROM user ORDER BY id;")
        for u in all_users:
            print(f"ID:{u['id']}, 姓名:{u['username']}, 性别:{u['gender']}, 电话:{u['phone']}")

    def add_user(self, id, username, gender, phone):
        sql = "INSERT INTO user (id, username, gender, phone) VALUES (%s, %s, %s, %s)"
        self.db.exec(sql, (id, username, gender, phone))

    def get_user_by_id(self, id):
        sql = "SELECT * FROM user WHERE id=%s"
        user = self.db.query(sql, (id,))
        if user:
            print(f"查询结果 -> ID:{user[0]['id']}, 姓名:{user[0]['username']}, 电话:{user[0]['phone']}")
        else:
            print("未找到该用户")

    def update_user_phone(self, id, phone):
        sql = "UPDATE user SET phone=%s WHERE id=%s"
        self.db.exec(sql, (phone, id))

    def delete_user(self, id):
        sql = "DELETE FROM user WHERE id=%s"
        self.db.exec(sql, (id,))

if __name__ == '__main__':
    db = DBHelper()
    um = UserManager(db)

    um.show_all("初始表内容")

    um.add_user(4, '赵六', '女', '13300000000')
    um.show_all("执行add后的内容")

    print("\n--- 执行get_user_by_id后的内容 ---")
    um.get_user_by_id(4)

    um.update_user_phone(4, '18888888888')
    um.show_all("执行update_user_phone后的内容")

    um.delete_user(4)
    um.show_all("执行delete_user后的内容")