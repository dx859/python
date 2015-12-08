words = ['cat', 'dog', 'annimal']

# for
for w in words:
    print(w, len(w))

# range()函数
for i in range(len(words)):
    print(i, words[i])

# range(m, n, step) // m,n,step 起始，结束，步长，包括其实不包括结束
for i in range(1, 5, 2):
    print(i)

# break 和 continue 语句, 以及循环中的 else 子句
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

# 循环可以有一个 else 子句；它在循环迭代完整个列表（对于 for ）或执行条件为 false （对于 while ）时执行，但循环被 break 中止的情况下不会执行。
# 注意：else 语句是属于 for 循环之中， 不是 if 语句
# 与循环一起使用时，else 子句与 try 语句的 else 子句比与 if 语句的具有更多的共同点：try 语句的 else 子句在未出现异常时运行，循环的 else 子句在未出现 break 时运行。

# pass 语句什么也不做。它用于那些语法上必须要有什么语句，但程序什么也不做的场合
pass # ...
# 这通常用于创建最小结构的类:
class MyEmptyClass:
    pass

# pass 可以在创建新代码时用来做函数或控制体的占位符。可以让你在更抽象的级别上思考。pass 可以默默的被忽视
def initlog(*args):
    pass