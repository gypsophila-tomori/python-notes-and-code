# Python程序语法元素分析

## 1.缩进

一个tab或者四个空格

## 2.注释

用于提高可读性

```Python
## 这是单行注释
''' 这是多行注释开头
这是多行注释结尾'''
```

## 3.变量

保存或表示数据的占位符号

```Python
tempstr = "32F" //这是一个变量的赋值方式，“=”是赋值符号
```

变量名可以是``大小写字母`` ``数字`` ``下划线`` ``中文字符``的组合
大小写敏感
不能是保留字（关键字），比如``if`` ``elif`` ``else`` ``in`` 等

## 4.数据类型

数据类型：``字符串`` ``整数`` ``浮点`` ``列表``
**e.g.温度转换**

```Python
#TempConvert.py
TempStr = input("请输入带有符号的温度值: ")
if TempStr[-1] in ['F', 'f']:
    C = (eval(TempStr[0:-1]) - 32)/1.8
    print("转换后的温度是{:.2f}C".format(C))
elif TempStr[-1] in ['C', 'c']:
    F = 1.8*eval(TempStr[0:-1]) + 32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误")
```

### **(1)字符串**：

**由0个或者多个字符组成的有序字符序列**  
用"双引号"或者'单引号'表示  
字符串是有序序列，``"ABCD1234"``中"A"是第0个字符  
可以正向或者反向排序  
索引：返回字符串中的单个字符  ``<字符串>[M]``
``tempstr[-1]``  
切片：返回字符串中的字符子串 ``<字符串>[M:N]``
``tempstr[1:3]``    ``tempstr[0:-1]``

## 5.语句

**(1)赋值语句给变量赋予新的数据值**
``C=(eval(tempstr[0:-1])-32)/1.8``
``tempstr=input("")``  
input返回字符串，所以tempstr也是字符串  
赋值语句都是用``=``构成的代码

**(2)分支语句**
判断程序运行的方向

## 6.函数

``print("input error")``

``eval(tempstr[0:-1])``

都是函数
使用``import``导入函数库例如

```python
import numpy as np
import ultralytics
import ollama
```

**(1)输入函数**
``input()``
变量 = input("提示")

**(2)输出函数**
向控制台输出结果
print(<输出的变量或字符串>)

```python
print("转换后温度为{:.2f }C".format(C))转换为浮点数
```

``{}``为“槽”，后续变量填充到槽中，``{:.2f}``表示将C填充进去后取小数点后两位

**(3)评估函数**
eval(<字符串或字符变量>)

```python
eval('1')
```

结果为1

```python
eval("1+2")
```

输出结果为3

```python
eval(tempstr[0:-1])
```

如果tempstr为12.4
输出结果为12.4

## 实战：蟒蛇绘制

```Python
#PythonDraw.py
import turtle #导入绘图库海龟库(turtle)
turtle.setup(650, 350, 200, 200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
turtle.done()
```

**turtle库**
Python的标准库之一，需要通过``import turtle``加载
窗口是离散的，最小单位是像素(pixel)
屏幕左上角为``(0,0)``，窗体左上角为``startx,starty``的坐标
``turtle.setup(width,hight,startx,starty)``

```Python
import libname
import libname2 as l2

libname.fun()
ls.fun2()
```

## 循环语句
```Python
for i in range(4)
    ……
```
``range(n)``产生一个n个数的序列，从0到n-1  
可以有步长