''' 
# 两个数进行计算
import my_calc

while True:
    # 输入两个数，错误格式返回
    try:
        num1 = int(input("请输入第一个数："))
    except ValueError:
        print("输入错误，请输入数字")
        continue

    try:
        num2 = int(input("请输入第二个数："))
    except ValueError:
        print("输入错误，请重新输入第一个数")
        continue

    # 进行选择，1加法，2减法，3乘法，4除法，5退出，错误格式返回
    try:
        print("1.加法")
        print("2.减法")
        print("3.乘法")
        print("4.除法")
        print("5.退出程序")
        choice = int(input("请选择运算类型："))

        if choice == 1:
            print(num1, "+", num2, "=", my_calc.add(num1, num2))
        elif choice == 2:
            print(num1, "-", num2, "=", my_calc.subtract(num1, num2))
        elif choice == 3:
            print(num1, "*", num2, "=", my_calc.multiply(num1, num2))
        elif choice == 4:
            print(num1, "/", num2, "=", my_calc.divide(num1, num2))
        elif choice == 5:
            print("退出程序")
            break
        else:
            print("无效选择，请输入1-5之间的数字")
    except ValueError:
        print("输入错误，请输入数字")
    except Exception as e:
        print("发生错误：", e)
'''

#生成随机验证码
import yanzhengma
code=yanzhengma.yanzhengma()
print(code)

#时间格式化输出
import datetime
now = datetime.now()
print(now.strftime("年%Y-月%m-日%d %H:%M:%S"))