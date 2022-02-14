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

任何 Python 序列都可迭代的原因是，它们都实现了 `__getitem__` 方法。其实，标准的序列也都实现了 `__iter__` 方法，因此你也应该这么做。之所以对 `__getitem__` 方法做特殊处理，是为了向后兼容，而未来可能不会再这么做（不过，写作本书时还未弃用）。

不过要注意，虽然前面定义的Sentence类是可以迭代的，但却无法通过 `issubclass (Sentence, abc.Iterable)` 测试（因为它没有实现 `__iter__` 方法）。

## 可迭代的对象与迭代器的对比
使用iter 内置函数可以获取迭代器的对象。如果对象实现了能返回迭代器的 `__iter__` 方法，那么对象就是可迭代的。序列都可以迭代；实现了 `__getitem__` 方法，而且其参数是从零开始的索引，这种对象也可以迭代。

**我们要明确可迭代的对象和迭代器之间的关系：Python 从可迭代的对象中获取迭代器**
```python
s = "ABC"
for i in s:
    print(i)
    
it = iter(s) # 获取可迭代对象 s 的迭代器 it

while True:
    try:
        print(next(it))
    except StopIteration:
        break

```
输出如下:
```
A
B
C
A
B
C
```
> 标准的迭代器接口有两个方法：`__next__` 返回下一个可用的元素，如果没有元素了，抛出 StopIteration 异常。`__iter__` 返回 self，以便在应该使用可迭代对象的地方使用迭代器，例如在for 循环中。

因为迭代器只需 `__next__` 和 `__iter__` 两个方法，所以除了调用next() 方法，以及捕获 StopIteration 异常之外，没有办法检查是否还有遗留的元素。此外，也没有办法“还原”迭代器。如果想再次迭代，那就要调用iter(...)，传入之前构建迭代器的可迭代对象

迭代器是这样的对象：实现了无参数的 `__next__`  方法，返回序列中的下一个元素；如果没有元素了，那么抛出 StopIteration  异常。Python中的迭代器还实现了 `__iter__` 方法，因此迭代器也可以迭代。

## 典型的迭代器版本
```python
class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
    
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    
    def __iter__(self):
        return SentenceIterator(self.words)

class SentenceIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0
    
    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word
    
    def __iter__(self):
        return self
        
s = Sentence('"The time has come," the Walrus said,') 
print(s)

for word in s:
    print(word)

print(issubclass(SentenceIterator, abc.Iterator))
    
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
True
['The', 'time', 'has', 'come', 'the', 'Walrus', 'said']
```
> 可迭代的对象一定不能是自身的迭代器。也就是说，可迭代的对象必须实现 `__iter__` 方法，但不能实现 `__next__` 方法。

## 生成器函数版本
看代码：
```python
class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
    
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    
    def __iter__(self):
        for word in self.words:
            yield word
s = Sentence('"The time has come," the Walrus said,') 
print(s)

for word in s:
    print(word)

print(issubclass(Sentence, abc.Iterable))
    
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
True
['The', 'time', 'has', 'come', 'the', 'Walrus', 'said']
```

只要 Python函数的定义体中有yield 关键字，该函数就是生成器函数。调用生成器函数时，会返回一个生成器对象。也就是说，生成器函数是生成器工厂。

生成器函数会创建一个生成器对象，包装生成器函数的定义体。把生成器传给 next(...) 函数时，生成器函数会向前，执行函数定义体中的下一个yield语句，返回产出的值，并在函数定义体的当前位置暂停。最终，函数的定义体返回时，外层的生成器对象会抛出 StopIteration 异常——这一点与迭代器协议一致。

## 惰性版本
```python
class Sentence:
    def __init__(self, text):
        self.text = text
    
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    
    def __iter__(self):
        for word in RE_WORD.finditer(self.text ):
            yield word.group()
s = Sentence('"The time has come," the Walrus said,') 
print(s)

for word in s:
    print(word)

print(issubclass(Sentence, abc.Iterable))
    
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
True
['The', 'time', 'has', 'come', 'the', 'Walrus', 'said']
```