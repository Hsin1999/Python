**Python**

python交互式编程

数据不保存

适用于简单的代码的验证

python console（控制台）也可以进行交互式编程

\#可以加注释，只对本行有效

''' 三个单引号开始，三个单引号结束，多行注释'''

快捷添加/取消注释 c+/

数字类型：int，float，complex

列表类型['1','2','3']

字典类型{'xx':'xx','xx':'xx'}

元组类型(1,2,3,4,5,6)

集合类型{1,'hello',true}

标识符命名规则：小驼峰命名法，大驼峰命名法，使用下划线连接

python里的变量，函数和模块用下划线连接，python里类名使用大驼峰命名法

print：

sep参数用来表示输出时，每个值之间使用哪种字符作为分隔。默认使用空格作为分隔符。

end当执行完一个print语句以后，接下来要输出的字符，默认/n表示换行。

二进制以0b开头

八进制以0o开头

十六进制以0x开头

进制转换：bin、oct、hex函数转换二进制、八进制、十六进制

转换成布尔值时，字符串中空字符串可以转换成false，整型只有0才可以转换成false，空数据None转换成布尔值是false、空字典、空列表、空集合、空元组会被转换成false

*表示可变长度

位运算：

&：按位与：同为1则为1，否则为0

｜：按位或：只要有一个为1，就为1

^：按位异或：相同为0，不同为1

～：按位取反：0变1，1变0

<<左移n位

\>>右移n位

逻辑运算优先级

：not>and>or

三元表达式：

x=num1 if num1>num2 else num2

range内置类用来生成指定区间的整数序列

range(0,10),包含开始’0’，不包含结束‘10’

for in 后面必须是一个可迭代对象

可迭代对象：字符串、列表、字典、元组、集合、range

for else:当循环里的break没有被执行的时候，就会执行else

\:转义字符

在字符串前加r表示输出原生字符 

Str list tuple可以通过下标来获取或操作数据，下标都是从0开始的

切片是从字符串里复制一段指定的内容，生成一个新字符串

切片[start|:end:step]，包含头不包含尾

Find 在字符串中找下标，若没有找到返回-1

Index 没有找到 报错

startswith，endswith

内容分割：

os.path.splitext():（分割成元组）os.path.splittext(path)[1]

split，rsplit（分割成列表）

partition，rpartition（分割成元组）

格式化代码：ctrl alt L

ctrl shift +上下箭头：将代码上下移动

判断：startswith,endswith,isalpha,isdigit,isalnum,isspace

capitalize:让第一个单词首字符大写

upper：让所有字母都大写

lower：让所有字母都小写

title：每个单词的首字母大写

ljust（width,fillchar）：让字符串以指定长度显示，若长度不够，默认用空格代替，fillchar可以来指定补齐的字符

rjust

center

去空格：lstrip,rstrip,strip

将列表转换成字符串：

"想加入的符号".join

字符串的编码：

chr：获取编码对应的字符

ord：获取字符对应的编码

GBK：国标扩，汉字占两个字节，简体中文

BIG5：繁体

UTF-8:统一编码，汉字占三个字节

查看编码：.encode("编码类型")

查看解码：.decode("编码类型")

格式化打印字符串

%s：字符串的占位符

%d：整数的占位符

%f：浮点数的占位符

%nd：显示n位，如果不够，默认使用空格补齐

%x：以16进制打印

%%：输出一个百分号

.format()：用{}占位

{}：根据数字的顺序来进行填入，数字从零开始，也可以填变量

列表:

可以使用list（可迭代对象）将可迭代对象转换成一个列表

list的增删改查

.append('xx')在最后边追加一个数据

.insert()在指定的位置插入数据

A.extend(B) 将可迭代对象B添加到A里面

删除：

.pop()默认删除列表里最后一个数据，可以传入index参数，用来删除指定位置上的数据

.remove()用来删除指定元素

.clear()删除所有数据

python数据都是放在内存里的

可变类型：列表，字典，集合

不可变类型：字符串，数字，元组

字典的遍历：

.items

.key

.values

外部库升级命令pip install xx



eval（）：将字符串转化成命令

json.dumps()函数是将一个Python数据类型列表进行json格式的编码（可以这么理解，json.dumps()函数是将字典转化为字符串）

json.loads()函数是将json格式数据转换为字典（可以这么理解，json.loads()函数是将字符串转化为字典）

enumerate（）获取列表的值及下标

globals()查看全局变量

locals()查看局部变量

python只有函数能分割作用域

*args：可变参数，以元组保存

**kwargs：可变关键字，以字典保存



**浅拷贝****(copy)****：**拷贝父对象，不会拷贝对象的内部的子对象。

**深拷贝****(deepcopy)****：** copy 模块的 deepcopy 方法，完全拷贝了父对象及其子对象

lambda匿名函数：a,b:a+b（只能写一条表达式）

filter(函数，可迭代对象)过滤数据 结果为iterator，需要用list（）转换才能输入

map(函数，可迭代对象)把每一个值都执行函数中的内容

reduce(函数，列表)将数据加到一块，列表后可加初始值





Import Hashlib

Import hmac 

Hashlib支持的算法md5，sha

md5只支持将二进制加密

.hexdigest()：将hash变为16进制编码

uuid：全局唯一id

Pip freeze 查看当前安装列表及版本号

pip freeze >输出到指定地址



__name__在自己的py下运行值为__main__，被当模块调用时值为文件名

正则表达式：

https://www.runoob.com/python/python-reg-expressions.html

.span():显示搜索到的字符串所在位置

match：从头开始匹配

search：在整个字符串进行匹配

finditer：查找到的所有匹配数据放到一个可迭代对象里

findall：把查找到的所有字符串结果放到一个列表里

fullmatch：完全匹配，整个字符串都要符合匹配的规则

Group（）：对正则使用()进行分组， 以分组形式查看

groupdict（）：给分组起名字 （?P<>），查看所有标签分组

re.sub(pattern, repl, string, count=0, flags=0)

参数：

- ​	pattern : 正则中的模式字符串。
- ​	repl : 替换的字符串，也可为一个函数。
- ​	string : 要被查找替换的原始字符串。
- ​	count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。

正则修饰符：对正则表达式进行修饰

. 表示除了换行以外的任意字符

re.S:让.匹配换行

re.I:忽略大小写

re.M:让$匹配到换行

[0-9][a-z][A-Z]

|:表示或者

{n,}:前面的元素出现n次以上

{,n}:前面的元素出现n次以下

{m,n}:前面的元素出现m次以上n次以下

*：表示前面的元素出现任意次

+：表示前面的元素出现1次以上

？:1、规定前面的元素最多只能出现一次

2、将贪婪模式转换成为费贪婪模式

^:以指定的内容开头

$:以指定的内容结尾

\n:换行

\t:表示一个制表符

\s:空白字符

\S:非空白字符

\d:表示数字

\D:非数字

\w:非标点符号

\W:标点符号

文件读写操作

r:只读模式,如果文件不存在会报错

w:写入模式，只能写入不能读取，如果文件存在会覆盖，文件不存在会创建

b:已二进制形式打开文件，可以用来操作非文本文件

rb:以二进制读取 wb:已二进制写入

a:追加模式，会在最后追加内容。如果文件不能存在，会创建文件；如果文件存在会追加。

r+:可读写

w+:可读写

t:以文本形式打开

..\:上一级目录

Readline:只读取一行数据

Readlines:读取数据，放入一个列表

Read(len):读取文件一定的长度

.rstrip('\n')删除字符串后面的\n

标准输入输出：

stdin：输入

stdout：输出

stderr：报错输出

a.readline().rstrip('\n')忽略\n

Csv文件的的读写：

writerow（）：写入一行，list列表方式

Writerows（）：写入多行

csv.reader（file）：读取所有数据，用for in可以查看，以列表方式展示



stringIO:将数据写入到内存

bytesIO：将数据以二进制的形式写入



类的使用：

class Animal:

​    \#通过构造方法定义类的属性

​    def __init__(self,name,age):

​      self.name=name

​      self.age=age

​    \# 定义类的方法

​    def sit(self):

​      \#模拟动物被命令坐下这个动作

​      print(self.name+" is now sitting. ")

\# 实例化——通过类得到对象

dog=Animal('Xiaohua',3)

print(dog.name)

print(dog.age)

Xiaohua

3

dog.sit()

Xiaohua is now sitting.

\# 实例化——得到其他对象

cat=Animal('Mimi',2)

cat.name

'Mimi'

cat.sit()

Mimi is now sitting.

类的继承

\#继承

class Dog(Animal):

  pass #占位符

\#父类：Animal，子类：Dog

jinmao=Dog('xiaojin',5)

jinmao.name

'xiaojin'

jinmao.sit()

xiaojin is now sitting.

\# 重写

class Dog(Animal):

  def sit(self):

​    print(self.name+" is now sitting,My age is %d"%self.age)

hashiqi=Dog('xiaoha',2)

hashiqi.name

'xiaoha'

hashiqi.sit()

xiaoha is now sitting,My age is 2

\# 模块其实也是类

from pandas import Series





\#实例化

ser1=Series(data=[4,7,-5,3])

ser1.values

array([ 4, 7, -5, 3], dtype=int64)

ser1.sum()

9

\#datetime,日期和时间

from datetime import datetime



dt1=datetime(2019,1,1)

print(dt1)



dt2=datetime(2019,1,1,12,30,45)

print(dt2)

2019-01-01 00:00:00

2019-01-01 12:30:45

dt2.day

1

dt2.minute

30

print(dt2.date())

2019-01-01

\#strptime

string_dt ='2019-1-1'

print(type(string_dt))

print(datetime.strptime(string_dt,'%Y-%m-%d'))

<class 'str'>



config.ini读写:https://www.cnblogs.com/ming5218/p/7965973.html

pytest：

fixture详细用法：

https://blog.csdn.net/totorobig/article/details/111823208

fixture的作用范围



fixture里面有个scope参数可以控制fixture的作用范围：session>module>class>function



-function：每一个函数或方法都会调用



-class：每一个类调用一次，一个类中可以有多个方法



-module：每一个.py文件调用一次，该文件内又有多个function和class



-session：是多个文件调用一次，可以跨.py文件调用，每个.py文件就是module



fixture调用方法：https://www.cnblogs.com/gaidy/p/13176695.html

设置函数：@pytest.fixture

调用函数：@pytest.mark.usefixture()

Console常用参数介绍：

-v 用于显示每个测试函数的执行结果

-q 只显示整体测试结果

-s 用于显示测试函数中print()函数输出

-x, --exitfirst, exit instantly on first error or failed test

-m 只运行带有装饰器配置的测试用例

-h 帮助

selenium元素定位：

https://blog.csdn.net/weixin_36279318/article/details/79475388