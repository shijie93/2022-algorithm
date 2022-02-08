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
实现 `__call__` 方法的类是创建函数类对象的简便方式，此时必须在内部维护一个状态，让它在调用之间可用。