# 关键字 def 引入了一个函数 定义。在其后必须跟有函数名和包括形式参数的圆括号。函数体语句从下一行开始，必须是缩进的。
def fib(n):
    """Print a Fibonacci series up to n.""" # 函数体的第一行语句可以是可选的字符串文本，这个字符串是函数的文档字符串，或者称为 docstring
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(200)
# 没有 return 语句的函数确实会返回一个值 None
print(fib(200))

def fib2(n):
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

print(fib2(100))


# 默认参数值  
def ask_ok(prompt, retries=4, complaint="Yes or no,please!"):
    while True:
        ok = input(prompt) 
        if ok in ('y', 'ye', 'yes'): # in 关键字。它测定序列中是否包含某个确定的值
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise OSError('uncooperative user')
        print(complaint)

# ask_ok('Do you really want to quit?')

#重要警告: 默认值只被赋值一次。这使得当默认值是可变对象时会有所不同，这个有点像闭包的概念
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# 如果你不想让默认值在后续调用中累积，你可以像下面一样定义函数
def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f2(1))
print(f2(2))
print(f2(3))

# 可变参数列表
def write_multiple_items(str, *args):
    arr = list(range(*args))
    print(arr)
write_multiple_items('name', 12,32,43)