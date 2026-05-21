def 手动平方根(x):
    if x == 0:
        return 0
    a = x
    b = (a + 1) / 2
    while abs(b - a) > 1e-10:  # 1e-10是一个很小的数，用于控制精度
        a = b
        b = (a + x / a) / 2
    return b

while True:
    边1 = input("请输入第一个直角边的长度：")
    边2 = input("请输入第二个直角边的长度：")
    
    if 边1.isdigit() and 边2.isdigit():
        边1 = float(边1)
        边2 = float(边2)
        斜边平方 = 边1**2 + 边2**2
        斜边 = 手动平方根(斜边平方)
        print(f"斜边的长度是：{斜边}")
        break
    else:
        print("输入无效，请确保输入的是数字。")
