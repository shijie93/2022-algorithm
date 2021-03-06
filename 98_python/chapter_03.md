# 字典和集合

**散列表** 则是字典类型性能出众的根本原因

标准库里的所有映射类型都是利用dict 来实现的，因此它们有个共同的限制，即只有可散列的数据类型才能用作这些映射里的键（只有键有这个要求，值并不需要是可散列的数据类型）。

## 可散列的数据类型
如果一个对象是可散列的，那么在这个对象的生命周期中，它的散列值是不变的，而且这个对象需要实现`__hash__()`方法。另外可散列对象还要有`__eq__()`方法，这样才能跟其他键做比较。如果一个对象是可散列的，那么在这个对象的生命周期中，它的散列值是不变的，而且这个对象需要实现`__hash__()`方法。另外可散列对象还要有`__eq__()`方法，这样才能跟其他键做比较。

> 如果一个对象是可散列的，那么在这个对象的生命周期中，它的散列值是不变的，而且这个对象需要实现__hash__()方法。另外可散列对象还要有__eq__()方法，这样才能跟其他键做比较。

## 字典创建的不同方式

常用方法：
```python
a1 = dict(one=1, two=2)
a2 = {'one':1, 'two':2}
a3 = dict(zip(['one','two'], [1,2]))
a4 = dict([('one', 1), ('two', 2)])

assert a1 == a2 == a3 == a4
```
也可以使用字典推导创建字典

## 用setdefault处理找不到的键

```python
a = dict()

a.setdefault('one', []).append(1)
a # {'one': [1]}
```

如果 a 中没有 one，则将 `one:[]`插入字典，并且返回 value，链式 `append`

## 映射的弹性键查询
### defaultdict
使用 defaultdict 完成上一例子相同的效果。
```python
from collections import defaultdict

a = defaultdict(list)
a['one'].append(1)
dict(a) # {'one': [1]}
```

> 在实例化一个 `defaultdict` 的时候，需要给构造方法提供一个可调用对象，这个可调用对象会在`__getitem__` 碰到找不到的键的时候被调用，让`__getitem__ `返回某种默认值。如果在创建 `defaultdict` 的时候没有指定 default_factory，查询不存在的键会触发 KeyError。

### 特殊方法 `__missing__`

`__missing__` 方法只会被__getitem__ 调用（比如在表达式 `d[k]`中）。提供 `__missing__` 方法对get或者`__contains__`（`in` 运算符会用到这个方法）这些方法的使用没有影响。

```python
class NewDict(dict):
    
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

a = NewDict()
a['2'] = 3
a['3'] = 4

print(a[2], a['2']) # 3 3
```

## 不可变映射类型

从Python 3.3开始，types 模块中引入了一个封装类名叫 MappingProxyType。如果给这个类一个映射，它会返回一个只读的映射视图。虽然是个只读视图，但是它是动态的。这意味着如果对原映射做出了改动，我们通过这个视图可以观察到，但是无法通过这个视图对原映射做出修改。

```python
from types import MappingProxyType

a = {'one': 1}
A = MappingProxyType(a)

A # mappingproxy({'one': 1})
A['one'] # 1

# A['two'] = 2 # TypeError: 'mappingproxy' object does not support item assignment

a['two'] = 2
A # mappingproxy({'one': 1, 'two': 2})
```

## 集合
如果要创建一个空集，你必须用不带任何参数的构造方法 set()。如果只是写成 {}的形式，跟以前一样，你创建的其实是个空字典。

像 `{1, 2, 3}`这种字面量句法相比于构造方法（`set([1, 2, 3])`）要更快且更易读。后者的速度要慢一些，因为Python 必须先从set 这个名字来查询构造方法，然后新建一个列表，最后再把这个列表传入到构造方法里。但是如果是像 `{1, 2, 3}` 这样的字面量，Python 会利用一个专门的叫作 `BUILD_SET` 的字节码来创建集合。

## dict的实现及其导致的结果

**键必须是可散列的**

1. 支持 hash()函数，并且通过__hash__() 方法所得到的散列值是不变的。
2. 支持通过__eq__() 方法来检测相等性。
3. 若 a == b 为真，则 hash(a) == hash(b) 也为真。

所有由用户自定义的对象默认都是可散列的，因为它们的散列值由 id() 来获取，而且它们都是不相等的。

**字典在内存上的开销巨大**

**键查询很快**

**键的次序取决于添加顺序**

**往字典里添加新键可能会改变已有键的顺序**
无论何时往字典里添加新的键，Python解释器都可能做出为字典扩容的决定。扩容导致的结果就是要新建一个更大的散列表，并把字典里已有的元素添加到新表里。这个过程中可能会发生新的散列冲突，导致新散列表中键的次序变化。如果你在迭代一个字典的所有键的过程中同时对字典进行修改，那么这个循环很有可能会跳过一些键——甚至是跳过那些字典中已经有的键。**由此可知，不要对字典同时进行迭代和修改。如果想扫描并修改一个字典，最好分成两步来进行：首先对字典迭代，以得出需要添加的内容，把这些内容放在一个新字典里；迭代结束之后再对原有字典进行更新。**

