# 继承的优缺点

## 子类化内置类型
内置类型（使用C语言编写）不会调用用户定义的类覆盖的特殊方法。

```python
class DoppelDict(dict):
    def __setitem__(self, k, v):
        print("调用重载后的 __setitem__")
        super().__setitem__(k, [v] * 2)

dd = DoppelDict(one=1) #1
print(dd)

dd['two'] = 2 #2
print(dd)

dd.update(three=3) #3 
print(dd)
```

输出如下：
```
{'one': 1}
调用重载后的 __setitem__
{'one': 1, 'two': [2, 2]}
{'one': 1, 'two': [2, 2], 'three': 3}
```

我们可以清晰的看到，1和3都没有调用重载后的 `__setitem__`（由来自内置类型的`__init__` 和 `update` 间接调用），而 2 因为是直接调用的，所以调用了重载的方法。原生类型的这种行为违背了面向对象编程的一个基本原则：始终应该从实例（self）所属的类开始搜索方法，即使在超类实现的类中调用也是如此。

**直接子类化内置类型（如dict、list或str）容易出错，因为内置类型的方法通常会忽略用户覆盖的方法。不要子类化内置类型，用户自己定义的类应该继承 collections 模块中的类，例如UserDict、UserList和UserString，这些类做了特殊设计，因此易于扩展。**

集成 UserDict 则可以解决上述问题：
```python
from collections import UserDict
class DoppelDict(UserDict):
    def __setitem__(self, k, v):
        print("调用重载后的 __setitem__")
        super().__setitem__(k, [v] * 2)

dd = DoppelDict(one=1)
print(dd)

dd['two'] = 2
print(dd)

dd.update(three=3)
print(dd)
```

输出如下：
```
调用重载后的 __setitem__
{'one': [1, 1]}
调用重载后的 __setitem__
{'one': [1, 1], 'two': [2, 2]}
调用重载后的 __setitem__
{'one': [1, 1], 'two': [2, 2], 'three': [3, 3]}
```

> 综上，本节所述的问题只发生在C语言实现的内置类型内部的方法委托上，而且只影响直接继承内置类型的用户自定义类。如果子类化使用Python 编写的类，如UserDict或MutableMapping，就不会受此影响。

## 多重继承和方法解析顺序
```python
class A:
    def ping(self):
        print('ping', 'A', self)

class B(A):
    def pong(self):
        print('pong', 'B', self)

class C(A):
    def pong(self):
        print('PONG', 'C', self)

class D(B, C):
    def ping(self):
        super().ping()
        print('post-ping','D', self)
    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)
```
Python 能区分 d.pong() 调用的是哪个方法，是因为Python 会按照特定的顺序遍历继承图。这个顺序叫方法解析顺序（Method Resolution Order，MRO）。类都有一个名为 `__mro__` 的属性，它的值是一个元组，按照方法解析顺序列出各个超类，从当前类一直向上，直到object类。D类的 `__mro__` 属性如下：

```python
D.__mro__ # (__main__.D, __main__.B, __main__.C, __main__.A, object)
```

若想把方法调用委托给超类，推荐的方式是使用内置的super()函数。 然而，有时可能需要绕过方法解析顺序，直接调用某个超类的方法——这样做有时更方便。例如，D.ping 方法可以这样写：
```python
    def ping(self):
        A.ping(self)
        print('post-ping','D', self)
```
注意，直接在类上调用实例方法时，必须显式传入 self 参数，因为这样访问的是未绑定方法。然而，使用super() 最安全，也不易过时。调用框架或不受自己控制的类层次结构中的方法时，尤其适合使用super()。使用super() 调用方法时，会遵守方法解析顺序。

看看调用D实例的 pingping方法输出：
```python
d = D()
d.pingpong()
```
输出如下：
```
ping A <__main__.D object at 0x7f4983940790>
post-ping D <__main__.D object at 0x7f4983940790>
ping A <__main__.D object at 0x7f4983940790>
pong B <__main__.D object at 0x7f4983940790>
pong B <__main__.D object at 0x7f4983940790>
PONG C <__main__.D object at 0x7f4983940790>
```

通过查看类的 `__mro__` 可以查看类的方法搜索顺序：
```python
import numbers
numbers.Integral.__mro__
# (numbers.Integral,
# numbers.Rational,
# numbers.Real,
# numbers.Complex,
# numbers.Number,
# object)
```

如果一个类的作用是为多个不相关的子类提供方法实现，从而实现重用，但不体现“是什么”关系，应该把那个类明确地定义为混入类（mixin class）。从概念上讲，混入不定义新类型，只是打包方法，便于重用。混入类绝对不能实例化，而且具体类不能只继承混入类。混入类应该提供某方面的特定行为，只实现少量关系非常紧密的方法。

