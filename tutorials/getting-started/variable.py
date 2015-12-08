# 整数与浮点


# 字符串

# 1. 使用 r'' 表示''内部的字符串默认不转义
print(r'\\n\\')
# 2. 如果字符串内部有很多换行，用\n写在一行里不好阅读，Python允许用'''...'''的格式表示多行内容
print('''line1
line2
line3''')
# 3. 多行字符串'''...'''还可以在前面加上r使用
print(r'''line1
\\
line2''')
# 4. 可以使用 + 拼接字符串或字符串与变量

# 布尔值 True False
# 布尔值可以用and、or和not运算。(not 是非运算符)

# None

# 变量
# python中的变量不需要声明，但必须初始化（赋值）

# 通过 Python，可以使用 ** 运算符计算幂乘方
print('5 ** 2=',5 ** 2)

# 在交互模式中最近一个表达式的值赋给变量 _。
'''
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
'''
# 注意：python没有多行注释，可以使用'''...'''字符串来包裹


# 字符串可以用来截取（检索）字符串的第一个字符索引为 0 。Python没有单独的字符类型；一个字符就是一个简单的长度为1的字符串
word = 'Python'
print(word[0])
name = '张三'
print(name[1])

# 索引也可以是负数，这将导致从右边开始计算
print(word[-1])
# 除了索引，还支持 切片。索引用于获得单个字符，切片 让你获得一个子字符串
print(word[2:4]) # 包含起始的字符，不包含末尾的字符
# 切片的索引有非常有用的默认值；省略的第一个索引默认为零，省略的第二个索引默认为切片的字符串的大小。
print(word[:2])
print(word[2:])
print(word[-2:])
# 注意：索引起始不能越界，否则会出现错误，但Python 能够优雅地处理那些没有意义的切片索引
# word[32]会出错，但 word[2:32]不会
print(word[2:32])
# Python字符串不可以被更改 — 它们是 不可变的 。因此，赋值给字符串索引的位置会导致错误:
# word[0] = 'J' ：TypeError: 'str' object does not support item assignment
# 如果你需要一个不同的字符串，你应该创建一个新的
# 内置函数 len() 返回字符串长度
print(len(word))