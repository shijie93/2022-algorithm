# 序列的修改、散列和切片

先构建一个 Vector 类：
```python
from array import array
import reprlib
import math

class Vector:
    typecode = 'd'
    
    def __init__(self, components):
        self._components = array(self.typecode, components)
    
    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)
    
    def __str__(self):
        return str(tuple(self))
    
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(self._components))
    
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    
    def __abs__(self):
        return math.sqrt(sum(x*x for x in self))
    
    def __bool__(self):
        return bool(abs(self))
    
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)
```


## 序列协议和鸭子类型
在面向对象编程中，协议是非正式的接口，只在文档中定义，在代码中不定义。例如，Python的序列协议只需要 `__len__`和_`_getitem__` 两个方法。任何类（如Spam），只要使用标准的签名和语义实现了这两个方法，就能用在任何期待序列的地方。Spam是不是哪个类的子类无关紧要，只要提供了所需的方法即可。

比如对于下面这个类：
```python
import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])
class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suitsfor rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]
```
虽然并未集成序列父类，但是他实现了 `__len__`和_`_getitem__` 两个方法，任何有经验的Python 程序员只要看一眼就知道它是序列，即便它是object的子类也无妨。我们说它是序列，因为它的行为像序列，这才是重点。协议是非正式的，没有强制力，因此如果你知道类的具体使用场景，通常只需要实现一个协议的部分。例如，为了支持迭代，只需实现 `__getitem__` 方法，没必要提供 `__len__` 方法。

## 支持切片

```python
from array import array
import reprlib
import math

class Vector:
    typecode = 'd'
    
    def __init__(self, components):
        self._components = array(self.typecode, components)
    
    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)
    
    def __str__(self):
        return str(tuple(self))
    
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(self._components))
    
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    
    def __abs__(self):
        return math.sqrt(sum(x*x for x in self))
    
    def __bool__(self):
        return bool(abs(self))
    
    def __len__(self):
        return len(self._components)
    
    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, int):
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))
    
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

v7 = Vector(range(7))
v7[-1] # 6.0
v7[1:4] # Vector([1.0, 2.0, 3.0])
```

得益于 Vector 构造函数支持可迭代对象，所以在传入 slice 时，直接重新构造对象即可(self._components[1:4] 是可迭代对象)。

## 动态存储属性

简单来说，对 `my_obj.x`表达式，Python 会检查 my_obj 实例有没有名为x的属性；如果没有，到类（`my_obj.__class__`）中查找；如果还没有，顺着继承树继续查找。 如果依旧找不到，调用my_obj所属类中定义的__getattr__ 方法，传入 self和属性名称的字符串形式（如'x'）。

多数时候，如果实现了`__getattr__` 方法，那么也要定义 `__setattr__` 方法，以防对象的行为不一致。

## 散列
添加散列特殊函数：
```python
import functools
import operator

    def __eq__(self, other):
        return len(self) == len(other) and all(a==b for a,b in zip(self, other))
    
    def __hash__(self):
        hashes = map(hash, self._components)
        return functools.reduce(operator.xor, hashes, 0) # 对 +、|和^ 来说， initializer 应该是0；而对 *和& 来说，应该是1。
    
```

