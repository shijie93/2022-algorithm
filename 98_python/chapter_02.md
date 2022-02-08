# 序列构成的数组

Python 标准库用C 实现了丰富的序列类型，列举如下。

**容器序列**

list、tuple和collections.deque 这些序列能存放不同类型的数据。

**扁平序列**

str、bytes、bytearray、memoryview和array.array，这类序列只能容纳一种类型。

> 容器序列存放的是它们所包含的任意类型的对象的引用，而扁平序列里存放的是值而不是引用。换句话说，扁平序列其实是一段连续的内存空间。由此可见扁平序列其实更加紧凑，但是它里面只能存放诸如符、字节和数值这种基础类型。

序列类型还能按照能否被修改来分类。

**可变序列**

list、bytearray、array.array、collections.deque和memoryview。

**不可变序列**

tuple、str和bytes

## 列表推导和生成器表达式
列表推导是构建列表（list）的快捷方式，而生成器表达式则可以用来创建其他任何类型的序列。如果
你的代码里并不经常使用它们，那么很可能你错过了许多写出可读性更好且更高效的代码的机会。

> 列表推导、生成器表达式，以及同它们很相似的集合（set）推导和字典（dict）推导，在Python 3中都有了自己的局部作用域，就像函数似的。表达式内部的变量和赋值只在局部起作用，表达式的上下文里的同名变量还可以被正常引用，局部变量并不会影响到它们。

列表推导如下：
```python
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
[(color, size) for color in colors for size in sizes]
```

输出如下:
```
[('black', 'S'),
 ('black', 'M'),
 ('black', 'L'),
 ('white', 'S'),
 ('white', 'M'),
 ('white', 'L')]
```

虽然也可以用列表推导来初始化元组、数组或其他序列类型，但是生成器表达式是更好的选择。这是因为生成器表达式背后遵守了迭代器协议，可以逐个地产出元素，而不是先建立一个完整的列表，然后再把这个列表传递到某个构造函数里。前面那种方式显然能够**节省内存**。

生成器表达式如下：
```python
symbols = '$¢£¥€¤'
tuple(ord(symbol) for symbol in symbols)
```

输出如下：
```
(36, 162, 163, 165, 8364, 164)
```

>  如果生成器表达式是一个函数调用过程中的唯一参数，那么不需要额外再用括号把它围起来。生成器表达式逐个产出元素，当元素数量很庞大时，使用列表推导会占用很大一片内存用以存放元素，而生成器表达式会一次产生元素，是内存友好的方法。


## 元组不仅仅是不可变的列表

元组其实是对数据的记录：元组中的每个元素都存放了记录中一个字段的数据，外加这个字段的位置。正是这个位置信息给数据赋予了意义。如果只把元组理解为不可变的列表，那其他信息——它所含有的元素的总数和它们的位置——似乎就变得可有可无。但是如果把元组当作一些字段的集合，那么数量和位置信息就变得非常重要了。如果在任何的表达式里我们在元组内对元素排序，这些元素所携带的信息就会丢失，因为这些信息是跟它们的位置有关的。

### 元组拆包
```python
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
```

元组拆包可以应用到任何可迭代对象上，唯一的硬性要求是，被可迭代对象中的元素数量必须要跟接受这些元素的元组的空档数一致。

另外一个很优雅的写法当属不使用中间变量交换两个变量的值：`b, a = a, b`

还可以用 \* 运算符把一个可迭代对象拆开作为函数的参数：
```python
t = (20, 8)
divmod(*t)
```

函数也可以返回元组：
```python
import os
_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
```

> 在进行拆包的时候，我们不总是对元组里所有的数据都感兴趣，`_ `占位符能帮助处理这种情况。

用 \* 来处理剩下的元素:
```python
a, b, *rest = range(5) # (0, 1, [2, 3, 4])
```

> \* 前缀只能用在一个变量名前面，但是这个变量可以出现在赋值表达式的任意位置

### 具名元组
collections.namedtuple是一个工厂函数，它可以用来构建一个带字段名的元组和一个有名字的类——这个带名字的类对调试程序有很大帮助。用namedtuple 构建的类的实例所消耗的内存跟元组是一样的，因为字段名都被存在对应的类里面。这个实例跟普通的对象实例比起来也要小一些，因为Python 不会用__dict__ 来存放这些实例的属性。

定义和使用具名元组：
```python
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.population, tokyo[2])
print(City._fields)
c = City._make(tokyo)
c._asdict()
```

输出如下：
```
City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722, 139.691667))
36.933 36.933
('name', 'country', 'population', 'coordinates')
{'name': 'Tokyo',
 'country': 'JP',
 'population': 36.933,
 'coordinates': (35.689722, 139.691667)}
```

> `_fields` 属性是一个包含这个类所有字段名称的元组.用`_make()` 通过接受一个可迭代对象来生成这个类的一个实例，它的作用跟`City(*delhi_data)`是一样的。`_asdict()` 把具名元组以 `collections.OrderedDict`的形式返回，我们可以利用它来把元组里的信息友好地呈现出来。

## 切片

序列翻转：
```python
s = 'bicycle'
s[::-1]
```

给切片命名：
```python
a = '320x11199x08060551'
year = slice(6, 10)
month = slice(11, 13)
```

切片赋值：
```python
l = list(range(10))
l[2:5] = [20, 30] # [0, 1, 20, 30, 5,6,7,8,9]
del l[5:7] # [0, 1, 20, 30, 5,8,9]

# [0, 1, 20, 30, 5,6,7,8,9] # error
```

>  如果赋值的对象是一个切片，那么赋值语句的右侧必须是个可迭代对象。即便只有单独一个值，也要把它转换成可迭代的序列

## 序列复制的陷阱
```python
board = [['_'] * 3 for i in range(3)]
board[1][2] = 'X'
print(board)

board = [['_'] * 3] * 3
board[1][2] = 'X'
print(board)
```

输出如下：
```
[['_', '_', '_'], ['_', '_', 'X'], ['_', '_', '_']]
[['_', '_', 'X'], ['_', '_', 'X'], ['_', '_', 'X']]
```

后者子列表其实是同一个列表的三个引用

## 序列的增量赋值

`+=` 背后的特殊方法是`__iadd__` （用于“就地加法”）。但是如果一个类没有实现这个方法的话，Python会退一步调用`__add__`。如果 a 实现了`__iadd__` 方法，就会调用这个方法。同时对可变序列（例如list、bytearray和array.array）来说，a 会就地改动，就像调用了a.extend(b) 一样。但是如果 a 没有实现 `__iadd__`的话，a+= b 这个表达式的效果就变得跟a = a + b 一样了：首先计算 a + b，得到一个新的对象，然后赋值给 a 。也就是说，在这个表达式中，变量名会不会被关联到新的对象，完全取决于这个类型有没有实现 `__iadd__`这个方法。
 
对比列表和元组的增量赋值：
```python
l = [1, 2, 3]
print(id(l))
l += [5,6]
print(id(l))

l = (1, 2, 3)
print(id(l))
l += (5,6)
print(id(l))
```

输出如下：
```
139972458766784
139972458766784
139973003895488
139972455370000
```

> 对不可变序列进行重复拼接操作的话，效率会很低，因为每次都有一个新对象，而解释器需要把原来对象中的元素先复制到新的对象里，然后再追加新的元素。

## 一个关于+=的谜题
考虑如下代码：
```python
a = (1,2,[30,40,50])
a[2] += [60,70]
```

思考运行结果如何？解释器会抛出异常 `TypeError: 'tuple' object does not support item assignment`，但是 a 的值仍然变为 `(1, 2, [30, 40, 50, 60, 70])`。

> 不要把可变对象放在元组里面。

> 增量赋值不是一个原子操作。如上，它虽然抛出了异常，但还是完成了操作

## 数组
如果我们需要一个只包含数字的列表，那么 array.array 比 list 更高效。数组支持所有跟可变序列有关的操作，包括 `.pop`
、`.insert`和`.extend`。另外，数组还提供从文件读取和存入文件的更快的方法，如`.frombytes`和`.tofile`。
Python 数组跟C语言数组一样精简。创建数组需要一个类型码，这个类型码用来表示在底层的C语言应该存放怎样的数据类型。比如b
类型码代表的是有符号的字符（signed char），因此 array('b') 创建出的数组就只能存放一个字节大小的整数，范围从-128 到127，这样在序列很大的时候，我们能节省很多空间。而且Python 不会允许你在数组里存放除指定类型之外的数据。

```python
from array import array
from random import random

arr = array('d', (random() for _ in range(10 ** 2)))

fp = open('data.bin', 'wb')
arr.tofile(fp)
fp.close()

arr2 = array('d')
fp2 = open('data.bin', 'rb')
arr2.fromfile(fp2, 10**2)
fp2.close()

assert arr2 == arr
assert arr2[-1] == arr[-1]
```

既快，占用空间又小。

## collections.deque
利用.append和.pop 方法，我们可以把列表当作栈或者队列来用（比如，把 .append和.pop(0) 合起来用，就能模拟队列的“先进先出”的特点）。但是删除列表的第一个元素（抑或是在第一个元素之前添加一个元素）之类的操作是很耗时的，因为这些操作会牵扯到移动列表里的所有元素。

collections.deque类（双向队列）是一个线程安全、可以快速从两端添加或者删除元素的数据类型。而且如果想要有一种数据类型来存放“最近用到的几个元素”，deque 也是一个很好的选择。

```python
from collections import deque

dq = deque(range(10), 10)
print(dq)

dq.appendleft(-1)
print(dq)

dq.pop()
print(dq)

dq.insert(2, 22)
print(dq)
```

输出如下：
```
deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
deque([-1, 0, 1, 2, 3, 4, 5, 6, 7, 8], maxlen=10)
deque([-1, 0, 1, 2, 3, 4, 5, 6, 7], maxlen=10)
deque([-1, 0, 22, 1, 2, 3, 4, 5, 6, 7], maxlen=10)
```

> append和popleft 都是原子操作，也就说是deque 可以在多线程程序中安全地当作先进先出的队列使用，而使用者不需要担心资源锁的问题。