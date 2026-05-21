'''
str = 'abbbcccddddeeeeeefffffff'
'''
'''
print(str.find('c'))
print(str.rfind('c'))
print(str.rfind('e'))
print(str.index('f'))
print(str.rindex('d'))
print(str.count('f'))
'''
'''
for i, j in enumerate(str):
    if i == str.index(j):
        print((i, j, str.count(j)), end=' ')
'''
'''
print(str.split('d'))
print(str.rsplit('d'))
print(str.partition('d'))
print(str.rpartition('d'))
print(str.rpartition('d'))
'''
'''
table=''.maketrans('abcde', '12345')
s='how are you nice to meet you'
print(s.translate(table))
count=1
for i in s:
    if i in ' ':
        count+=1
print(count)
'''
'''
#输出标准英文格式
test='hello world! I like python. this is a nice day. right?'
print(test.lower())
print(test.upper())
print(test.capitalize())
print(test.title())
print(test.swapcase())
result = test.lower()
result = result[0].upper() + result[1:]
i = 1
while i < len(result):
    if result[i] in '.!?' and i + 2 < len(result):
        result = result[:i+2] + result[i+2].upper() + result[i+3:]
    i += 1
print('修改后的文本：', result)
#统计单词数量
words=test.split()
print('单词个数：',len(words))
#对文本进行加密，每个字母替换为后面k个
k=3
'''
'''
result=''
for i in test:
    if 'a'<= i <= 'z':
        result += chr((ord(i) - ord('a') + k) % 26 + ord('a'))
    elif 'A' <= i <= 'Z':
        result += chr((ord(i) - ord('A') + k) % 26 + ord('A'))
    else:
        result += i
print('加密后的文本：',result)
'''
'''
str_lower = 'abcdefghijklmnopqrstuvwxyz' 
str_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
char=str_lower[k:]+str_lower[:k]+str_upper[k:]+str_upper[:k]
print('加密字符表：',char)
print('加密后的文本：',test.translate(str.maketrans(str_lower+str_upper,char)))
'''
'''
test = 'hello world! I like python. this is a nice day. right?'
k = 3
def format(t):
    result = t.lower()
    result = result[0].upper() + result[1:]
    i = 1
    while i < len(result):
        if result[i] in '.!?' and i + 2 < len(result):
            result = result[:i+2] + result[i+2].upper() + result[i+3:]
        i += 1
    return result

def count(t):
    return len(t.split())

def jm(t, k):
    l = 'abcdefghijklmnopqrstuvwxyz' 
    u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    c = l[k:] + l[:k] + u[k:] + u[:k]
    return t.translate(str.maketrans(l + u, c))

def menu():
    print("\n输入要执行的操作：")
    print("1. 输出标准英文格式")
    print("2. 统计单词数量")
    print("3. 密码加密 (k=3)")
    print("0. 退出程序")



while True:
    menu()
    c = input("请输入要执行的操作数字：")

    if c == '1':
        print("\n标准格式输出：")
        print("lower():", test.lower())
        print("upper():", test.upper())
        print("capitalize():", test.capitalize())
        print("title():", test.title())
        print("swapcase():", test.swapcase())
        print("修改后的文本：", format(test))
    
    elif c == '2':
        print("\n单词统计：")
        print("单词个数：", count(test))
    
    elif c == '3':
        print("\n加密 (k={}):".format(k))
        l = 'abcdefghijklmnopqrstuvwxyz'
        u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        print("加密字符表：", l[k:] + l[:k] + u[k:] + u[:k])
        print("加密后的文本：", jm(test, k))
    
    elif c == '0':
        print("程序已退出")
        break
    
    else:
        print("输入无效，请重新输入！")
'''

'''#strip()函数的使用
text='aaabbbcccddddeeeeeeffffff'
print(text.strip('af'))
print(text.lstrip('acf'))
print(text.rstrip('acf'))
'''
"""str.strip()函数的使用
text='''姓名：张三
年龄：25
性别男
职业 学生
籍贯：地球'''
infomation=text.split("\n")
print(infomation)
for i in infomation:
    print(i[:2],i[2:].strip('： '),sep=': ')
"""

'''#string模块的使用
import string
print(string.digits)
print(string.punctuation)
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)'''

'''#随机密码生成原理
import string
import random
mima = string.punctuation + string.ascii_letters + string.digits
#输入密码长度
while True:
    length = int(input("请输入密码长度："))
    if length >= 6:
        break
    else:
        print("密码长度必须至少为6，请重新输入")

#第一位是符号
for i in range(length-1):   
    password = random.choice(string.punctuation)
for i in range(length-1):
    password += random.choice(mima)
print("生成的密码是：", password)'''


'''s='hello world!\n文本文件的读取方法\n文本文件的写入方法\n'
with open('sample.txt', 'w', encoding='utf-8') as fp:
    fp.write(s)
with open('sample.txt', 'r', encoding='utf-8') as fp:
    content = fp.read()
    print(content)'''

'''s='hello world!\n文本文件的读取方法\n文本文件的写入方法\n'
with open('sample.txt', 'r', encoding='utf-8') as fp:
    s = fp.read(5)
print('s=',s)
print('字符串s的长度(字符个数)= ',len(s))

with open('sample.txt', encoding='utf-8') as fp:
    for line in fp:
        print(line, end='')'''

'''#先用文件操作函数写入数据，再进行读取排序，读取文本文件data.txt中的数字，升值排序后写入data_new.txt文件中
with open('data.txt', 'w', encoding='utf-8') as fp:
    fp.write('5\n3\n8\n1\n4\n')
with open('data.txt', 'r', encoding='utf-8') as fp:
    numbers = [int(line.strip()) for line in fp]
numbers.sort()
with open('data_new.txt', 'w', encoding='utf-8') as fp:
    for num in numbers:
        fp.write(str(num) + '\n')'''

'''#os和os.path模块的使用
import os
#获取当前目录
print(os.getcwd())
#获取指定目录的绝对路径
print(os.path.abspath('.'))
#获取指定目录的父目录
print(os.path.dirname(os.path.abspath('.')))
#获取指定目录的名称
print(os.path.basename(os.path.abspath('.')))
#获取当前目录下的所有文件和文件夹
print(os.listdir(os.getcwd()))
#获取当前目录下的所有.py文件
print([f for f in os.listdir(os.getcwd()) if f.endswith('.py')])'''


'''import os

def search_file(start_dir, target_filename):
    # os.walk 会自动遍历 start_dir 及其所有子目录
    # root: 当前目录路径
    # dirs: 当前目录下的子目录列表
    # files: 当前目录下的文件列表
    found = False

    for root, dirs, files in os.walk(start_dir):
        if target_filename in files:
            # 拼接完整路径
            full_path = os.path.join(root, target_filename)
            print(f"找到文件: {full_path}")
            found = True
            # 如果只需要找第一个匹配的文件，可以在这里 break 或 return

    if not found:
        print(f"在目录 '{start_dir}' 下未找到文件 '{target_filename}'")

if __name__ == "__main__":
    # 1. 获取用户输入
    directory = input("请输入要搜索的目录路径: ").strip()
    filename = input("请输入要查找的文件名 (包含扩展名): ").strip()

    # 2. 简单的输入验证
    if not os.path.isdir(directory):
        print("错误：输入的目录路径无效或不存在！")
    else:
        # 3. 执行搜索
        search_file(directory, filename)'''

