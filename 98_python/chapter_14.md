# 可迭代的对象、迭代器和生成器

迭代是数据处理的基石。扫描内存中放不下的数据集时，我们要找到一种惰性获取数据项的方式，即按需一次获取一个数据项。这就是迭代器模式（Iterator pattern）。

所有生成器都是迭代器，因为生成器完全实现了迭代器接口。迭代器用于从集合中取出元素；而生成器用于“凭空”生成元素。

在Python中，所有集合都可以迭代。在Python语言内部，迭代器用于支持：
* for 循环
* 构建和扩展集合类型
* 逐行遍历文本文件
* 列表推导、字典推导和集合推导
* 元组拆包
* 调用函数时，使用* 拆包实参


## Sentence类第1版：单词序列
定义一个可以逐个迭代单次的 Sentence类。第1版要实现序列协议。
```python
import re
import reprlib

RE_WORD=re.compile('\w+')

class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
    
    def __getitem__(self, index):
        return self.words[index]
    
    def __len__(self):
        return len(self.words)
    
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
s = Sentence('"The time has come," the Walrus said,') 
print(s)

for word in s:
    print(word)

list(s)
```
输出如下：
```
Sentence('"The time ha... Walrus said,')
The
time
has
come
the
Walrus
said
['The', 'time', 'has', 'come', 'the', 'Walrus', 'said']
```

**序列可以迭代的原因：iter函数**

解释器需要迭代对象 x 时，会自动调用iter(x)，内置的iter函数有以下作用：

(1) 检查对象是否实现了 `__iter__` 方法，如果实现了就调用它，获取一个迭代器。

(2) 如果没有实现 `__iter__` 方法，但是实现了 `__getitem__` 方法，Python 会创建一个迭代器，尝试按顺序（从索引 0开始）获取元素。

(3) 如果尝试失败，Python 抛出 TypeError 异常，通常会提示“C object is not iterable”（C对象不可迭代），其中C是目标对象所属的类。