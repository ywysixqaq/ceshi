#生成随机验证码（包含数字和大写字母，长度为6位）
import random

def yanzhengma():
    chr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    yzm = ''.join(random.choices(chr, k=6))
    return yzm

if __name__ == '__main__':
    yzm = yanzhengma()
    print(yzm)