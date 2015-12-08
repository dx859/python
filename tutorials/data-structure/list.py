'''
list.append(x) : 把一个元素添加到链表的结尾，相当于 a[len(a):] = [x]。
list.extend(L) : 将一个给定列表中的所有元素都添加到另一个列表中，相当于 a[len(a):] = L。
list.insert(i,x) : 在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，而 a.insert(len(a), x) 相当于 a.append(x)。
list.remove(x) : 删除链表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。
list.pop([i]) : 从链表的指定位置删除元素，并将其返回。如果没有指定索引，a.pop() 返回最后一个元素。
list.clear() : 从列表中删除所有元素。相当于 del a[:]。
list.index(x) : 返回链表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。
list.count(x) : 返回 x 在链表中出现的次数。
list.sort() : 对链表中的元素就地进行排序。
list.reverse() : 就地倒排链表中的元素。
list.copy() : 返回列表的一个浅拷贝。等同于 a[:]。
'''

a = [66.25, 333, 333, 1, 1234.5]
a[len(a):] = [123];
a.append(123)
b = ['hello', 'world']
a[len(a):] = b
a.extend(b)
a.insert(0, 'first');
print(a)
del a[:]
print(a)

# 链表当作堆栈，或者队列使用

# 列表推导式
squares = []
for x in range(10):
    squares.append(x ** 2)

print(squares)
# 注意这个 for 循环中的被创建(或被重写)的名为 x 的变量在循环完毕后依然存在
print(x)

# Python中，迭代永远是取出元素本身，而非元素的索引。
# 如果我们确实想在 for 循环中拿到索引，方法是使用 enumerate() 函数
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in enumerate(L):
    print(index, '-', name)

# 迭代字典
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
for k in d:
    print(k, '-', d[k])

for k, v in d.items():
    print(k, '-', v)

# 迭代dict中的value
for v in d.values():
    print(v)

# 生成列表 注意python3.x中range()需要list
print(list(range(1, 11)))

print([i * (i+1) for i in range(1,10,2)])

# 字符串可以通过 % 进行格式化，用指定的参数替代 %s。字符串的join()方法可以把一个 list 拼接成一个字符串。
tds = ['<tr><td>%s</td><td>%s</td></tr>' % (name, score) for name, score in d.items()]
print('<table>')
print('<tr><th>Name</th><th>Score</th><tr>')
print('\n'.join(tds))
print('</table>')