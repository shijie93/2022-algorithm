# 接口：从协议到抽象基类

先看下面这个例子：
```python
class Foo:
    def __getitem__(self, pos):
        return range(0, 30, 10)[pos]
    
f = Foo()
print(f[1])

for i in f:
    print(i)

print(20 in f)
print(15 in f)
```

输出如下：
```
10
0
10
20
True
False
```

虽然没有 `__iter__` 方法，但是Foo 实例是可迭代的对象，因为发现有 `__getitem__` 方法时，Python 会调用它，传入从0开始的整数索引，尝试迭代对象（这是一种后备机制）。尽管没有实现 `__contains__` 方法，但是Python 足够智能，能迭代Foo 实例，因此也能使用in 运算符：Python 会做全面检查，看看有没有指定的元素。综上，鉴于序列协议的重要性，如果没有 `__iter__`和 `__contains__` 方法，Python 会调用 `__getitem__`方法，设法让迭代和in 运算符可用。

## 使用猴子补丁在运行时实现协议
猴子补丁：在运行时修改类或模块，而不改动源码。猴子补丁很强大，但是打补丁的代码与要打补丁的程序耦合十分紧密，而且往往要处理隐藏和没有文档的部分。

```python
import random
import collections

Cards = collections.namedtuple('Cards', ['rank', 'suit'])
class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Cards(rank, suit) for suit in self.suits for rank in self.ranks ]
    
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, pos):
        return self._cards[pos]
    
    def __repr__(self):
        return str(self._cards)

def set_card(deck, position, card):
    deck._cards[position] = card
FrenchDeck.__setitem__ = set_card # 猴子补丁
f = FrenchDeck()
random.shuffle(f)
```

如果不添加猴子补丁，则在 shuffle 时会报错：`TypeError: 'FrenchDeck' object does not support item assignment`，原因是没有实现可变序列特殊方法 `__setitem__`。