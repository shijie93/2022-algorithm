# 对象引用、可变性和垃圾回收

变量最好把它们理解为附加在对象上的标注

每个变量都有标识、类型和值。对象一旦创建，它的标识绝不会变；你可以把标识理解为对象在内存中的地址。is 运算符比较两个对象的标识；id()函数返回对象标识的整数表。

对象 ID的真正意义在不同的实现中有所不同。在CPython中，id() 返回对象的内存地址，但是在其他Python解释器中可能是别的值。关键是，ID 一定是唯一的数值标注，而且在对象的生命周期中绝不会变。这也是为什么自行创建的类的hash值可用 hash(id)。

## ==和is
`==` 运算符比较两个对象的值（对象中保存的数据），而 is 比较对象的标识。

`is` 运算符比 `==` 速度快，因为它不能重载，所以 Python 不用寻找并调用特殊方法，而是直接比较两个整数 ID。而`a == b`是语法糖，等同于`a.__eq__(b)`。继承自 object的 `__eq__`方法比较两个对象的ID，结果与 is一样。但是多数内置类型使用更有意义的方式覆盖了`__eq__` 方法，会考虑对象属性的值。相等性测试可能涉及大量处理工作，例如，比较大型集合或嵌套层级深的结构时。

## 元组的相对不变性
如果引用的元素是可变的，即便元组本身不可变，元素依然可变。也就是说，元组的不可变性其实是指 tuple 数据结构的物理内容（即保存的引用）不可变，与引用的对象无关。

所以，元组虽然是不可变的，但是它是否可散列还要取决于内部引用的元素是否可变，只有当元素都不可变时，元组才是可散列的。
```python
a = dict()

a[(1,2)] = 3 # (1,2) 可散列
# a[(1,[1])] = 3 # 报错。因为(1,[1]]) 不可散列
```


## 默认做浅复制
看下面这个例子：
```python
a = [1,2,3,[4,5]]
b = list(a)

a is b # F
a == b # T
a[3] is b[3] # T
```
list(l1) 创建 l1 的副本。这是一种浅复制（即复制了最外层容器，副本中的元素是源容器中元素的引用）。如果所有元素都是不可变的，那么这样没有问题，还能节省内存。但是，如果有可变的元素，可能就会导致意想不到的问题。上例中 a b 中的子列表是同一对象，修改其中一个会影响另一个。

再看如下的例子：
```python
a = [1,[2,3,4],(5,6,7)]
b = list(a)
a.append(100)
a[1].remove(3)
print('a', a)
print('b', b)
b[1] += [55,66]
b[2] += (88,99)
print('a', a)
print('b', b)
```

输出如下：
```
a [1, [2, 4], (5, 6, 7), 100]
b [1, [2, 4], (5, 6, 7)]
a [1, [2, 4, 55, 66], (5, 6, 7), 100]
b [1, [2, 4, 55, 66], (5, 6, 7, 88, 99)]
```

b[2] 的修改并没有影响到 a[2] 的原因是元组是不可变类型，增量赋值会创建新的对象。

浅复制容易操作，但是得到的结果可能并不是你想要的。

## 深复制
通过 `copy.deepcopy` 可以实现对象的深复制（迭代创建新的对象），copy.copy` 可以实现对象的浅复制

## 函数的参数作为引用时
Python 唯一支持的参数传递模式是共享传参（call by sharing）。共享传参指函数的各个形式参数获得实参中各个引用的副本。也就是说，函数内部的形参是实参的别名。，函数可能会修改作为参数传入的可变对象，但是无法修改那些对象的标识（即不能把一个对象替换成另一个对象）。

看下面这个例子：
```python
def func(a, b):
    a += b
    return a

# 第一组
a = 1
b = 2
func(a, b) # 3
a, b # 1, 2

# 第二组
a = [1,2]
b = [3,4]
func(a, b) # [1, 2, 3 ,4]
a, b # [1,2,3,4], [3,4]

# 第三组
a = (1,2)
b = (3,4)
func(a, b) # (1,2,3,4)
a,b # (1,2), (3,4)
```

* 对于第一组，对a重新赋值仅仅只是更改局部变量的引用，外部 a的引用内容不变
* 对于第二组，对列表进行增量复制，局部变量 a 所指向的对象发生改变，和外部a所指向的对象相同
* 对于第三组，对元组增量赋值，因为元组为不可变类型，所以增量赋值会重新创建对象，此时和外部a所指向的对象不同

### 不要使用可变类型作为参数的默认值
可选参数可以有默认值，这是Python函数定义的一个很棒的特性，这样我们的API在进化的同时能保证向后兼容。然而，我们应该避免使用可变的对象作为参数的默认值。

但是看下面这个例子：
```python
class Bus():
    def __init__(self, passengers=[]):
        self.passengers=passengers
    def pick(self, name):
        self.passengers.append(name)
    def drop(self, name):
        self.passengers.remove(name)
        
b = Bus()

b.pick("zhangsan")
b.pick("lisi")
print(b.passengers)

c = Bus()
print(c.passengers)

assert b.passengers is c.passengers
```

输出如下：
```
['zhangsan', 'lisi']
['zhangsan', 'lisi']
```

我们可以看到，新创建的 Bus 对象 c 并没有新增乘客，但是 成员变量 passengers 中包含了 Bus 对象 b 的 passengers内容。问题在于，没有指定初始乘客的 Bus 实例会共享同一个乘客列表。出现这个问题的根源是，默认值在定义函数时计算（通常在加载模块时），因此默认值变成了函数对象的属性。因此，如果默认值是可变对象，而且修改了它的值，那么后续的函数调用都会受到影响。这里只需要将可变默认值 `[]` 替换为 None 即可。

### 防御可变参数
这此我们传入一个可变参数；
```python
class Bus2():
    def __init__(self, passengers=None):
        if not passengers:
            self.passengers = []
        else:
            self.passengers=passengers
    def pick(self, name):
        self.passengers.append(name)
    def drop(self, name):
        self.passengers.remove(name)
        
basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
b = Bus2(basketball_team)

b.drop('Sue')
b.drop('Tina')

basketball_team # ['Maya', 'Diana', 'Pat']
```

我们的初衷是想要将 basketball_team 的副本传入构造函数， Bus2 实例对象可以单独维护乘客，而不是以外篡改篮球队的列表。这就是传入可变参数可能引发的意想不到的问题。除非这个方法确实想修改通过参数传入的对象，否则在类中直接把参数赋值给实例变量之前一定要三思，因为这样会为参数对象创建别名。如果不确定，那就创建副本。这样客户会少些麻烦。修改为以下方式：
```python
class Bus2():
    def __init__(self, passengers=None):
        if not passengers:
            self.passengers = []
        else:
            self.passengers=list(passengers)
    def pick(self, name):
        self.passengers.append(name)
    def drop(self, name):
        self.passengers.remove(name)
        
basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
b = Bus2(basketball_team)

b.drop('Sue')
b.drop('Tina')

basketball_team # ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
```

通过 list 创建副本而不是别名，同时也可以传入元组或者生成器等其他形式。

## del和垃圾回收

在CPython中，垃圾回收使用的主要算法是引用计数。实际上，每个对象都会统计有多少引用指向自己。当引用计数归零时，对象立即就被销毁：CPython 会在对象上调用__del__ 方法（如果定义了），然后释放分配给对象的内存。CPython　2.0 增加了分代垃圾回收算法，用于检测引用循环中涉及的对象组——如果一组对象之间全是相互引用，即使再出色的引用方式也会导致组中的对象不可获取。

```python
import weakref

s1 = {1,2,3}
s2 = s1

def bye():
    print("goodbye")

ender = weakref.finalize(s1, bye)
print(ender.alive)

del s1
print(ender.alive)

s2 = "123"
print(ender.alive)
```

或许你会发现难道 weakref.finalize 没有持有对 s1 的引用吗，为什么 s2 取消对集合的引用之后集合就销毁了？这里是因为 weakref.finalize 持有的是弱引用。

## 弱引用
正是因为有引用，对象才会在内存中存在。当对象的引用数量归零后，垃圾回收程序会把对象销毁。但是，有时需要引用对象，而不让对象存在的时间超过所需时间。这经常用在缓存中。弱引用不会增加对象的引用数量。引用的目标对象称为所指对象（referent）。因此我们说，弱引用不会妨碍所指对象被当作垃圾回收。

### WeakValueDictionary
WeakValueDictionary类实现的是一种可变映射，里面的值是对象的弱引用。被引用的对象在程序中的其他地方被当作垃圾回收后，对应的键会自动从WeakValueDictionary中删除。因此，WeakValueDictionary 经常用于缓存。

```python
from weakref import WeakValueDictionary

class Cheese:
    def __init__(self, kind):
        self.kind = kind
        
    def __repr__(self):
        return 'Cheese(%r)' % self.kind
    
stock = WeakValueDictionary()

cheeses = [Cheese('Red Leicester'), Cheese('Tilsit'),Cheese('Brie'), Cheese('Parmesan')]

for c in cheeses:
    stock[c.kind] = c

print(sorted(stock.keys()))

del cheeses
print(sorted(stock.keys()))

del c
print(sorted(stock.keys()))
```

输出如下：
```
['Brie', 'Parmesan', 'Red Leicester', 'Tilsit']
['Parmesan']
[]
```
为什么 `del cheeses` 之后并没有删除所有的弱引用对象呢？原因是在循环中，c 最后停留在了 Parmesan 对象上，此强引用并没有解除。

除此之外，还有 WeakKeyDictionary以及 WeakSet。这些集合，以及一般的弱引用，能处理的对象类型有限。set 实例可以作为所指对象，用户定义的类型也没问题，但是，int和tuple 实例不能作为弱引用的目标，甚至它们的子类也不行。这些局限基本上是CPython的实现细节，在其他 Python解释器中情况可能不一样。这些局限是内部优化导致的结果。



