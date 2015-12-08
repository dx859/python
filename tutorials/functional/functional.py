# 闭包
def count():
    fs = []
    for i in range(1, 4):
        def f(j=i):
            return j*j
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(), f2(), f3())
