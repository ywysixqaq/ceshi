import os

def write():
    print("\n--- 写入数据模式 ---")
    text = input("请输入一组数字（用空格或逗号隔开）：")
    list1 = text.replace(',', ' ').split()
    
    try:
        nums = [int(x) for x in list1]
        with open('data.txt', 'w', encoding='utf-8') as f:
            for n in nums:
                f.write(f"{n}\n")
        print(f"成功写入 {len(nums)} 个数字！")
    except ValueError:
        print("输入有误！请确保输入的都是整数。")

def read_old():
    print("\n--- 读取原始数据 ---")
    if not os.path.exists('data.txt'):
        print("文件不存在，请先选择【1】写入数据！")
        return
        
    with open('data.txt', 'r', encoding='utf-8') as f:
        list1 = [line.strip() for line in f if line.strip()]
    print(f"原始数据内容：{', '.join(list1)}")

def sort():
    print("\n--- 数据排序 ---")
    if not os.path.exists('data.txt'):
        print("原始数据文件不存在，请先选择【1】写入数据！")
        return

    with open('data.txt', 'r', encoding='utf-8') as f:
        nums = [int(line.strip()) for line in f if line.strip()]

    print("请选择排序方式：1.升序  2.降序  3.还原")
    opt = input("请输入选项 (1/2/3)：")

    if opt == '1':
        nums.sort()
        print("已选择：升序排列")
    elif opt == '2':
        nums.sort(reverse=True)
        print("已选择：降序排列")
    elif opt == '3':
        print("已选择：还原为原始顺序")
    else:
        print("输入无效，本次未进行排序操作！")
        return

    with open('data_new.txt', 'w', encoding='utf-8') as f:
        for n in nums:
            f.write(f"{n}\n")
    print("处理完成！结果已保存。")

def read_new():
    print("\n--- 读取排序后的数据 ---")
    if not os.path.exists('data_new.txt'):
        print("排序文件不存在，请先选择【3】进行排序并保存！")
        return
        
    with open('data_new.txt', 'r', encoding='utf-8') as f:
        list1 = [line.strip() for line in f if line.strip()]
    print(f"排序文件内容：{', '.join(list1)}")

def menu():
    while True:
        print("1. 写入数据")
        print("2. 读取原始数据")
        print("3. 数据排序并保存")
        print("4. 读取排序后的数据")
        print("0. 退出系统")
        
        opt = input("请输入功能编号：")
        
        if opt == '1':
            write()
        elif opt == '2':
            read_old()
        elif opt == '3':
            sort()
        elif opt == '4':
            read_new()
        elif opt == '0':
            print("感谢使用，再见！")
            break
        else:
            print("输入无效，请重新输入！")

if __name__ == '__main__':
    menu()