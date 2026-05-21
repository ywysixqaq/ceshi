'''import requests
resp = requests.get('https://httpbin.org/get')
print('类型(text)',type(resp.text))
data = resp.json()
print('类型(json)',type(data))'''

'''#响应状态码
import requests

resp = requests.get('https://httpbin.org/status/404')
print('状态码',resp.status_code)
try:
    resp.raise_for_status()
except requests.exceptions.HTTPError as e:
    print('出错了',e)'''

'''#网络异常处理
import requests
try:
    r=requests.get('https://httpbin.org/delay/2',timeout=999)
    r.raise_for_status()
    print('请求成功')
except requests.exceptions.Timeout:
    print('请求超时')
except requests.exceptions.RequestException as e:
    print('未知错误',e)'''

"""#使用requests库调用公开ip查询api
import requests

# 定义 API 地址
url = "http://httpbin.org/ip"

try:
    # 1. 发送标准的 HTTP GET 请求
    print("正在发送请求...")
    response = requests.get(url, timeout=0.5)
    
    # 2. 检查响应状态码
    print(f"响应状态码: {response.status_code}")
    
    if response.status_code == 200:
        
        # 3. 解析 JSON 数据
        # response.json() 方法会将返回的字符串转换为 Python 字典
        json_data = response.json()
        print(f"解析后的 JSON 数据: {json_data}")
        
        # 4. 提取并打印公网 IP
        # 从字典中获取 'origin' 键对应的值
        ip_address = json_data.get("origin")
        print(f"您的公网 IP 地址是: {ip_address}")
        
except requests.exceptions.Timeout:
    print("错误：请求超时，请检查网络连接。")
except requests.exceptions.ConnectionError:
    print("错误：连接失败，请检查网络或URL是否正确。")
except Exception as e:
    print(f"发生未知错误: {e}")"""

'''import requests
parms_base= {
    'city': '新余',
    'key':'b0e4f32c69fd65f7de9c207454157a06',
    'extension':'all',
    'output':'json'
}
try:
    res_base = requests.get('https://restapi.amap.com/v3/weather/weatherInfo',params=parms_base,timeout=10)
    data_base = res_base.json()
    print(data_base)
except requests.exceptions.Timeout:
    print("请求超时，请检查网络连接。")'''


"""import requests
from datetime import datetime

# 请求参数
parms_base = {
    'city': '新余',
    'key': 'b0e4f32c69fd65f7de9c207454157a06',
    'extension': 'all',
    'output': 'json'
}

try:
    # 发送请求
    res_base = requests.get('https://restapi.amap.com/v3/weather/weatherInfo', params=parms_base, timeout=10)
    data_base = res_base.json()

    # 检查请求是否成功
    if data_base['status'] == '1' and data_base['count'] != '0':
        # 解析数据
        live_data = data_base['lives'][0] # 实时天气数据
        
        # 格式化输出
        print("<time_location>")
        print(f"城市：{live_data['province']} {live_data['city']}")
        print(f"天气：{live_data['weather']}")
        print(f"当前时间：{datetime.now().strftime('%Y-%m-%d %A')}")
        print(f"当前地点：{live_data['province']} {live_data['city']}")
        print("</time_location>")
        
    else:
        print(f"请求失败：{data_base.get('info', '未知错误')}")

except requests.exceptions.Timeout:
    print("请求超时，请检查网络连接。")
except Exception as e:
    print(f"发生错误：{e}")"""


"""#定义类
class Student:
    school = "新余学院"
    
    def study(self):
        print(f"{self.school}的学生{self.name}正在学习...")


#创建对象
student1 = Student()
student2 = Student()
student1.name,student2.name = "小明","小红"
print(student1.school)
student1.study()"""



'''class Student:
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name

s=Student()
s.set_name("小明")
print(s.get_name())'''

"""#定义名为Car的类, 并设置color属性, 并定义run方法
class Car:
    color = "白色"          #类属性

    def run(self):
        print(f'一辆{self.color}的车正在行驶')

car1 = Car()        #创建对象
car2 = Car()
car2.color = "红色"
car1.run()      #调用run方法
car2.run()"""

"""class Student:
    school = "新余学院"     #类属性 所有学生共享
    def __init__(self, name):
        self.name = name         #实例属性 每个实例都有自己的属性值
s1 = Student("小明")
s2 = Student("小红")
#访问实例属性 结果不同
print(s1.name, s2.name)
#访问类属性 结果相同
print(s1.school)
print(Student.school)   
Student.school = "南昌大学"
#修改类属性 全局生效
print(s1.school, s2.school)"""


'''class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    @classmethod
    def create_square(cls, side):
        return cls(side, side)

a=Rectangle(5,3)
print(f'矩形的面积为{a.area()},周长为{a.perimeter()}')
b=Rectangle.create_square(4)
print(f'正方形的边长为{b.width},面积为{b.area()},周长为{b.perimeter()}')'''


'''class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age
        
    def set_age(self, age):
        if 0 < age < 150:
            self.__age = age
        else:
            print("年龄不合法")

p=Person("小明",20)
print(p.get_age())
p.set_age(160)'''


'''class Shape:
    def get_area(self):
        return 0
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def get_area(self):
        return self.side ** 2
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def get_area(self):
        return 3.14 * self.radius ** 2
    
def calculate_total_area(shapes_list):
    total=0
    for shape in shapes_list:
        total+=shape.get_area()
    return total


square_1=Square(4)
circle_2=Circle(2)
shapes_list=[square_1,circle_2]
total= calculate_total_area(shapes_list)
print(f"总面积为{total:.2f}")'''


#银行账户管理系统
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
            print(f"账户{self.account_id}的余额为{self.__balance}")
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
            print(f"账户{self.account_id}的密码修改为{new_password}")
        else:
            print("密码错误")


# --- 主程序与菜单部分 ---

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
    print("5. 退出系统")
    
    choice = input("请输入您的选择 (1-5): ")

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
        
        # 修改密码逻辑（加入8位长度限制）
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
        print("感谢使用，再见！")
        break
    else:
        print("输入无效，请重新输入！")