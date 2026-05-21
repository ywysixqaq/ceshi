'''
while True:
    输入 = input("请输入一个三位数：")
    if 输入.isdigit() and len(输入) == 3:
        数字 = int(输入)
        百位 = 数字 // 100
        十位 = (数字 // 10) % 10
        个位 = 数字 % 10
        print(f"百位是：{百位}, 十位是：{十位}, 个位是：{个位}")
        break
    else:
        print("请重新输入")
'''