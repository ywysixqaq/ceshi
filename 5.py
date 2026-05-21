
'''#os.walk()方法会生成一个三元组(root, dirs, files)，其中root表示当前正在访问的这个目录的路径，dirs是一个列表，包含了root下所有子目录的名字，files也是一个列表，包含了root下所有非目录文件的名字。
import os
def visidir2(path):
    if not os.path.isdir(path):
        print('Error:"',path, '"is not a directory or does not exist.')
        return
    list_dirs=os.walk(path)
    for root, dirs, files in list_dirs:
        print(root)
        for d in dirs:
            print(os.path.join(root,d))
        for f in files:
            print(os.path.join(root,f))

if __name__=='__main__':
    path=input('请输入要遍历的目录路径：')
    visidir2(path)'''


'''#统计一个目录下的文件总大小、文件数量和目录数量
import os
totalSize,fileNum,dirNum=0,0,0
def countSize(path):
    global totalSize,fileNum,dirNum
    if not os.path.isdir(path):
        print('Error:"',path, '"is not a directory or does not exist.')
        return
    list_dirs=os.walk(path)
    for root, dirs, files in list_dirs:
        for d in dirs:
            dirNum+=1
            countSize(os.path.join(root,d))  #递归调用，统计子目录的大小、文件数量和目录数量
        for f in files:
            fileNum+=1
            totalSize+=os.path.getsize(os.path.join(root,f))

if __name__=='__main__':
    path=input('请输入要统计的目录路径：')
    countSize(path)
    print(f'目录数量: {dirNum}')
    print(f'文件数量: {fileNum}')
    print(f'文件总大小: {totalSize}')'''



'''class ShortInputException(Exception):
    def __init__(self, length, atLeast):
        Exception.__init__(self)
        self.length = length
        self.atLeast = atLeast
try:
    s = input("请输入: ")
    if len(s) < 3:
        raise ShortInputException(len(s), 3)
except EOFError:
    print('你输入了一个结束标记EOF')
except ShortInputException as ex:
    print('ShortInputException: 输入的长度是%d，至少应该是%d' % (ex.length, ex.atLeast))
else:
    print('没有异常发生')'''

"""#输入一个数字，如果输入的不是数字，则提示用户重新输入，直到输入正确为止
while True:
    x=input('请输入: ')
    try:
        x=int(x)
        print('你输入的数字是:{0}'.format(x))
        break
    except Exception as e:
        print('输入的不是数字，请重新输入')"""


'''#输入一个学生成绩，判断是否合法，则提示用户重新输入，直到输入正确为止
while True:
    try:
        grade_input = input("请输入学生成绩(0-100): ")

        if not grade_input:
            raise ValueError("输入不能为空")

        grade = float(grade_input)

        # 检查成绩范围
        if grade < 0 or grade > 100:
            raise ValueError("成绩必须在0-100之间")

    except ValueError as e:
        # 处理输入异常
        if "could not convert" in str(e):
            print("错误：输入的成绩不能为字符，请重新输入数值")
        else:
            print(f"错误：{e}")
    except Exception as e:
        print(f"发生未知错误：{e}")
    else:
        # 成功输入后输出成绩
        print(f"学生的成绩是：{grade}")
        break'''

'''import json
user_data = {"name": "张三","age": 25,"skills": ["Python", "Java"]}
json_str = json.dumps(user_data,ensure_ascii=False,indent=4)
print('转换后的JSON字符串：',json_str)
parsed_dict = json.loads(json_str)
print('提取姓名：' , str(parsed_dict["name"]))
print('提取技能列表：' , str(parsed_dict["skills"]))
'''


import json
dict={
    "company": "Alibaba",
    "employees": [
        {"name": "Alice", "position": "Engineer", "salary": "10000"},
        {"name": "Bob", "position": "Manager", "salary": "15000"},
    ],
    "location": "Hangzhou"
}
#数据解析（json字符串解析为python字典）
json_str=json.dumps(dict,ensure_ascii=False,indent=4)
print('转换后的JSON字符串：',json_str)
#提取公司名称和所在地
parsed_dict=json.loads(json_str)
print('公司名称：' , str(parsed_dict["company"]))
print('所在地：' , str(parsed_dict["location"]))
#提取所有员工信息以及工资
for employee in parsed_dict["employees"]:
    print('员工姓名：' , str(employee["name"]))
    print('职位：' , str(employee["position"]))
    print('工资：' , str(employee["salary"]))