# 一等函数

在Python中，函数是一等对象。编程语言理论家把“一等对象”定义为满足下述条件的程序实体：
* 在运行时创建
* 能赋值给变量或数据结构中的元素
* 能作为参数传给函数
* 能作为函数的返回结果

构造一个斐波那契函数：
```python
def factorial(n):
    '''returns n!'''
    return 1 if n < 2 else n * factorial(n - 1)

print(factorial(42))
print(factorial.__doc__)
print(type(factorial))
```

输出如下：
```
1405006117752879898543142606244511569936384000000000
returns n!
<class 'function'>
```

我们可以看到，factorial 函数是类 function 的实例，拥有成员 `__doc__`。

也可以将函数赋值给其他变量：
```python
fact = factorial
print(fact(5))
print(list(map(fact, range(0,11))))
```

输出如下：
```
120
[1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
```

## 高阶函数
接受函数为参数，或者把函数作为结果返回的函数是高阶函数（higher-order function）。map，sorted 等都是高阶函数。如下例子演示根据单次尾字母排序：
```python
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
def reverse(word):
    return word[::-1]

sorted(fruits, key=reverse) # ['banana', 'apple', 'fig', 'raspberry', 'strawberry', 'cherry']
```

列表推导或生成器表达式具有map和filter 两个函数的功能，而且更易于阅读。Python 3以后基本可以代替。例如：
```python
assert list(map(fact, range(6))) == [fact(n) for n in range(6)] 
assert  list(map(factorial, filter(lambda n: n % 2, range(6)))) == [factorial(n) for n in range(6) if n % 2]
```

> 在Python 3中，map和filter 返回生成器（一种迭代器），因此现在它们的直接替代品是生成器表达式

## 匿名函数
lambda 关键字在Python表达式内创建匿名函数
```python
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
sorted(fruits, key=lambda x: x[::-1])
```
除了作为参数传给高阶函数之外，Python 很少使用匿名函数

> lambda 句法只是语法糖：与 def语句一样，lambda表达式会创建函数对象。这是Python中几种可调用对象的一种

## 可调用对象
Python中有各种各样可调用的类型，因此判断对象能否调用，最安全的方法是使用内置的callable()函数。

### 用户定义的可调用对象
实现 `__call__` 方法的类是创建函数类对象的简便方式，此时必须在内部维护一个状态，让它在调用之间可用。示例代码如下：
```python
class Test:
    def __call__(self):
        print("函数类对象被调用")
t = Test()
t() # print
```

## 函数的定位参数和仅限关键字参数

```python
def func(a, *b, c=None, **d):
    print(a, b, c, d)

func(1)
func(1, 2, 3, 4 ,5 ,6)
func(1, c=100)
func(1, f=22)
```
输出如下：
```
1 () None {}
1 (2, 3, 4, 5, 6) None {}
1 () 100 {}
1 () None {'f': 22}
```

> 定义函数时若想指定仅限关键字参数，要把它们放到前面有\*的参数后面。

如果不想支持数量不定的定位参数，但是想支持仅限关键字参数，在签名中放一个\* :
```python
def f(a, *, b):
    print(a, b)
    
f(1, b=2)
```
> 仅限关键字参数不一定要有默认值，可以像上例中 b 那样，强制必须传入实参

### 提取函数的签名
```python
def func(a, *b, c=20, **d):
    e = 10
    print(a, b, c, d)

from inspect import signature

sign = signature(func)
print(str(sign))
for name, param in sign.parameters.items():
    print(param.kind,':', name, '=', param.default)
```
输出如下：
```
(a, *b, c=20, **d)
POSITIONAL_OR_KEYWORD : a = <class 'inspect._empty'>
VAR_POSITIONAL : b = <class 'inspect._empty'>
KEYWORD_ONLY : c = 20
VAR_KEYWORD : d = <class 'inspect._empty'>
```
* POSITIONAL_OR_KEYWORD：可以通过定位参数和关键字参数传入的形参（多数 Python函数的参数属于此类）。
* VAR_POSITIONAL：定位参数元组。
* VAR_KEYWORD：关键字参数字典。
* KEYWORD_ONLY：仅限关键字参数（Python 3新增）。
* POSITIONAL_ONLY：仅限定位参数；目前，Python 声明函数的句法不支持，但是有些使用C语言实现且不接受关键字参数的函数（如divmod）支持。

## 支持函数式编程的包
### operator
operator 模块为多个算术运算符提供了对应的函数，从而避免编写 `lambda a, b: a*b` 这种平凡的匿名函数，下面是用 operator 实现斐波那契：
```python
from operator import mul
from functools import reduce

def fact(n):
    return reduce(mul, range(1, n+1))

fact(4)
```

operator 模块中还有一类函数，能替代从序列中取出元素或读取对象属性的lambda 表达式：因此，itemgetter 和attrgetter 其实会自行构建函数。

```python
from operator import itemgetter
metro_data = [
     ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)), 
     ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),    
     ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),   
     ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),     
     ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)), 
 ]

for city in sorted(metro_data, key=itemgetter(2)):
    print(city)
    
```

输出如下：
```
('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
('New York-Newark', 'US', 20.104, (40.808611, -74.020386))
('Mexico City', 'MX', 20.142, (19.433333, -99.133333))
('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889))
('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
```

上述结果按照每个元组的第三个元素排序

如果把多个参数传给 itemgetter，它构建的函数会返回提取的值构成的元组：
```python
cc_name = itemgetter(1, 0)
for city in metro_data:
    print(cc_name(city))
```

输出如下：
```
('JP', 'Tokyo')
('IN', 'Delhi NCR')
('MX', 'Mexico City')
('US', 'New York-Newark')
('BR', 'Sao Paulo')
```

attrgetter 用法与 itemgetter 类似，主要是针对具名元组：
```python
from collections import namedtuple
from operator import attrgetter

LatLong = namedtuple('LatLong', 'lat long')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')
metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long))
               for name, cc, pop, (lat, long)in metro_data]

name_lat = attrgetter('name', 'coord.lat')

for city in metro_areas:
    print(name_lat(city))
```

输出如下：
```
('Tokyo', 35.689722)
('Delhi NCR', 28.613889)
('Mexico City', 19.433333)
('New York-Newark', 40.808611)
('Sao Paulo', -23.547778)
```

methodcaller 的作用与 attrgetter和itemgetter类似，它会自行创建函数。methodcaller 创建的函数会在对象上调用参数指定的方法：
```python
from operator import methodcaller

repl = methodcaller('replace', ' ', '-')

repl('2022 02 03') # '2022-02-03'
```

### 使用functools.partial冻结参数

functools.partial 这个高阶函数用于部分应用一个函数。部分应用是指，基于一个函数创建一个新的可调用对象，把原函数的某些参数固定。使用这个函数可以把接受一个或多个参数的函数改编成需要回调的API，这样参数更少。

```python
from operator import mul
from functools import partial

mul_3 = partial(mul, 3)

[mul_3(i) for i in range(10)] # [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
```

