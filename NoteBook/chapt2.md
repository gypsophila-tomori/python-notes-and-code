# 基本数据类型

对象是Python的最基本概念，Python处理的都是对象  
数字`int` `float` `complex`  
字符串`srt`,比如`"Python"`  
字节串`bytes`,比如`` b'hello world' ``
列表`list`,比如[1,2,3]  
元组`tuple`,比如`(2,4,-1)`,`(3,)`不可变  
字典  
集合`set`,比如`{'a','b','c'}`  
内置函数,比如`sum()` `max()` `sorted()` `min()`  
非内置对象需要导入
```python
id(x)
```  
返回对象的地址

## 基本的数字类型
**`规范数字的表示和使用`**
### 1.整数类型
与数学一致
```python
pow(x,y)
```
求x^y  
进制转换：二进制`0b` 八进制`0o` 十六进制`0x`

### 2.浮点数
Python的浮点数值存在限制，浮点精度也存在限制  
不用限制与不同计算机有关
```python
import sys
sys.float_info
```
表示方式：  
·直接使用数字：`0.7` `0.9`  
·使用科学计数法：`9e4` `9.6e5`  
浮点运算存在不确定尾数，小数可以无限接近，但是不能精确表示，比较时要四舍五入

### 3.复数类型
与数学中一致`z=x+yj`

### 4.扩展
整数->浮点数->复数  
最宽类型，整数+浮点数=浮点数
```python
x+y #加
x-y #减
x*y #乘
x/y #求商
x//y #求整数商
x%y #求模
```
```python
abs(x)
divmod(x,y)
pow(x,y[z])
round([x,ndigits])
max(x1,x2,x3,x4……,xn)
min()
```
```python
int(x) #强制转换为整数
float(x) #强制转换为浮点数 float(4) = 4.0
complex(re[,im]) #强制转换为复数

#不允许conplex强制转换为float和int

type(x) 
#返回x的参数类型 
## type(4.5) 
## >>> <class float>
```

## math库和函数/实例一
math为Python内置的数学类函数库  
**注意，math库不支持复数类型**
```python
import math
# 用法：math.<b>()
math.ceil(10.2) #取整
```
```python
form math import floor
floor(10.2) #可以不再使用 math.<b>()
```
```python
math.pi     #π
math.e      #e，自然对数
math.inf    #无穷大
math.nan    #非浮点占位符
```
一共有16个常用数值表示函数  
一共有8个幂对数函数  
一共有16个三角函数

## 字符串类型和操作
转义符
```python
print("\"hello\"") #表示\之后有字符串内容
# \b 回退  \n 换行  \r 回车
```


## 字符串格式化/实例二
python字符试用Unicode统一编码