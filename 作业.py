'''#定义图书类
class Book:
    # 1. 构造方法：初始化属性
    def __init__(self, title, author, price):
        self.title = title    # 书名
        self.author = author  # 作者
        self.price = price    # 价格
    def show_info(self):
        print(f"图书信息 -> 书名：《{self.title}》, 作者：{self.author}, 价格：{self.price}元")

book1 = Book("Python入门", "李四", 59.5)
book1.show_info()'''



#完善银行账户系统
def get_valid_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("输入无效，请输入正确的数字！")

class Bank_account:
    def __init__(self, account_id, name, balance, password):
        self.name = name
        self.__balance = balance
        self.__password = password
        self.account_id = account_id
        print("银行账户创建成功")

    def yu_e(self, password):
        if self.__password == password:
            print(f"账户{self.account_id}的余额为{self.__balance:.2f}")
            return self.__balance
        else:
            print("密码错误")
            return None

    def cun(self, amount, password):
        if self.__password == password:
            if amount > 0:
                self.__balance += amount
                print(f"账户{self.account_id}成功存款{amount}元")
            else:
                print("存款金额必须大于0")
        else:
            print("密码错误")

    def qu(self, amount, password):
        if self.__password == password:
            if amount > 0:
                if self.__balance >= amount:
                    self.__balance -= amount
                    print(f"账户{self.account_id}成功取款{amount}元")
                else:
                    print("余额不足")
            else:
                print("取款金额必须大于0")
        else:
            print("密码错误")

    def change_password(self, password, new_password):
        if self.__password == password:
            self.__password = new_password
            print(f"账户{self.account_id}的密码修改成功")
        else:
            print("密码错误")

    def calculate_interest(self, months, password):
        if self.__password != password:
            print("密码错误")
            return

        rate = 0.015
        current_balance = self.__balance
        last_month_interest = 0

        for i in range(months):
            interest = current_balance * rate
            current_balance += interest
            last_month_interest = interest

        total_interest = current_balance - self.__balance

        print("\n--- 利息计算结果 ---")
        print(f"经过 {months} 个月后：")
        print(f"账户本息合计：{current_balance:.2f} 元")
        print(f"累计获得总利息：{total_interest:.2f} 元")
        print(f"第 {months} 个月的单月利息：{last_month_interest:.2f} 元")
        print("--------------------")

print("--- 开户 ---")
uid = input("请输入账号: ")
uname = input("请输入姓名: ")

while True:
    upass_1 = input("请设置密码(至少8位): ")
    if len(upass_1) < 8:
        print("密码长度不能少于8位，请重新设置！")
        continue
        
    upass_2 = input("请再次输入密码: ")
    if upass_1 == upass_2:
        upass = upass_1
        break
    else:
        print("两次输入的密码不一致，请重新设置！")

ubalance = get_valid_number("请输入初始余额: ")
user1 = Bank_account(uid, uname, ubalance, upass)

while True:
    print("\n--- 银行管理系统 ---")
    print("1. 存款")
    print("2. 取款")
    print("3. 查询余额")
    print("4. 修改密码")
    print("5. 计算利息")
    print("6. 退出系统")
    
    choice = input("请输入您的选择 (1-6): ")

    if choice == '1':
        amount = get_valid_number("输入存款金额: ")
        pwd_in = input("输入密码: ")
        user1.cun(amount, pwd_in)
    elif choice == '2':
        amount = get_valid_number("输入取款金额: ")
        pwd_in = input("输入密码: ")
        user1.qu(amount, pwd_in)
    elif choice == '3':
        pwd_in = input("输入密码: ")
        user1.yu_e(pwd_in)
    elif choice == '4':
        old_pwd = input("输入旧密码: ")
        while True:
            new_pwd_1 = input("输入新密码(至少8位): ")
            if len(new_pwd_1) < 8:
                print("密码长度不能少于8位，请重新输入！")
                continue
            new_pwd_2 = input("请再次输入新密码: ")
            if new_pwd_1 == new_pwd_2:
                user1.change_password(old_pwd, new_pwd_1)
                break
            else:
                print("两次输入的新密码不一致，请重新输入！")
    elif choice == '5':
        pwd_in = input("输入密码: ")
        if user1._Bank_account__password == pwd_in:
            months = int(get_valid_number("请输入想要查看第几个月的利息："))
            if months > 0:
                user1.calculate_interest(months, pwd_in)
            else:
                print("月份必须大于0")
        else:
            print("密码错误")
    elif choice == '6':
        print("感谢使用，再见！")
        break
    else:
        print("输入无效，请重新输入！")