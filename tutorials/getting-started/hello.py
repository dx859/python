# # -*- coding: utf-8 -*-
# 在python2版本中，默认是ASCII码，无法识别中文，需要在头文件上加入encoding:编码名
print('hello, world')

# print语句也可以跟上多个字符串，用逗号“,”隔开，就可以连成一串输出
# 注意：print会依次打印每个字符串，遇到逗号“,”会输出一个空格
print('The quick brown fox', 'jumps over', 'the lazy do')

# 输入：input()，可以让用户输入字符串
print('set your name：')
name = input()
print('hello', name+', welcome!')