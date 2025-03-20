yuan = (1,2,6)
print(yuan[1])
print(type(yuan))

zidian = { 'name':'虔扆',
           'age' : '19',
           'home': '黄山',
           'game': 'mc',
    }

print(zidian.get('name'))

del zidian['game']

print(zidian)

zidian['game'] = '仙剑四'

print(zidian)

哈希值不同每次运行的结果不同，在哈希表中的位置不同
s1 = {'a','b','c','d','e'}
print(s1)


s2 = {1, 2, 3, 4, 5}
print(s2)

哈希值一直在变化，结果不同
print(hash('1'))
print(hash('2'))
print(hash('3'))

print(hash(1))
print(hash(2))
print(hash(3))


li = [1,2,[3,4,5],6,7]
print(li)

print(li)
li2 = li
li2.append(10)
print(li2)
print(li)
print("li原地址：",id(li))
li[2].append(8)

print("li现地址：",id(li))
print(li)

def fun1(*args):
    print(args)
fun1("第一","第二")

def fun2(**dic):
    print(dic)
fun2(name = "fyy",age = "18")

def fun1():
    a = 4
    def fun2():
        nonlocal a
        a = 10
        print("a的值是:",a)
    fun2()
    print("a的值是:",a)
fun1()

fun = lambda a,b:a+b
print(fun(1,2))
    
items = ["Start", "Step1", "Step2","End"]
result = "->".join(f"{[x]}" for x in items)
print(result)
print(items)

"""result = list(map(lambda x: str(x) if isinstance(x, (int, float)) else x.upper(), mixed))
   Lambda函数：lambda x: A if 条件 else B
"""
mixed = [10, "apple",3.14,"Banana",True]
result = list(map(lambda x: str(x) if isinstance(x, (int, float)) else x.upper(), mixed))
print(result)

import builtins
print(builtins)

tup = (1,2,3,4)
print(tup)
a,b,c,d = tup
print(a,b,c,d)


def error_li():
    psd = input("输入六位以上的密码")
    if len(psd) >= 6:
        return "密码输入成功"
    raise Exception("密码输入失败")
##print(error_li())

try:
    print(error_li())
except Exception as e:
    print(e)


def test1(): #函数名只是储存内容的地址
    print("luck qy")
# test1()
# print(test1)
ou = test1 #函数名后不加（）便能修改地址用其他值进行调用
ou()

'''闭包调用参数'''
def outer(m):
    print("outer()函数中的值：",m)
    def inner(n):
        print("inner()函数中的值：",n)
        return m + n
    return inner
ou = outer(10)
return
print(ou(20))
print(ou(40))
print(ou(80))
每次都会调用一遍inner()函数

'''装饰器调用函数 '''     
def fun1():
    print("hy ed")
def fun2(fn):
    print("gd qy")
    fn()
fun2(fun1)

'''被装饰函数'''
def send():
    print("hy ed qy")

def fun1(fn):#fn为形参，往里面传入的是被修饰函数send()
    #包含原有功能和新功能
    def fun2():
        print("")
        fn()
    return fun2 #return fun2()
print(fun1(send))
ou = fun1(send)#调用小括号
ou()

语法糖
def outer(fn):
    def inner():
        print("hello")
        #执行被装饰的函数
        fn()
    return inner
不能加（），前者是引用，后者是调用，返回该函数要返回的值
@outer
def send():
    print("World")
send()
