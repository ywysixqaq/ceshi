a,b,c=map(str,input("输入：").split())

##list1=[a,b,c]
##list1.sort()
##for i in list1:
##    print(i)

if a>b:
    a,b=b,a
if b>c:
    b,c=c,b
if a>b:
    a,b=b,a
print(a,b,c)
