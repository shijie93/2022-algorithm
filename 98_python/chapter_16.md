# 协程

协程是指一个过程，这个过程与调用方协作，产出由调用方提供的值

## 基本协程示例

```python
def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print('-> coroutine received:', x)

my_coro = simple_coroutine()
print(next(my_coro)) 
print(my_coro.send(42)) # 因为send 方法的参数会成为暂停的yield表达式的值，所以，仅当协程处于暂停状态时才能调用send
 方法
```

输出如下：
```
-> coroutine started
None
-> coroutine received: 42
StopIteration:
```

协程的四个状态（通过 inspect 的 getgeneratorstate）：
* 'GEN_CREATED' 等待开始执行。
* 'GEN_RUNNING' 解释器正在执行。
* 'GEN_SUSPENDED'在yield表达式处暂停。
* 'GEN_CLOSED' 执行结束

最先调用next(my_coro)函数这一步通常称为“预激”（prime）协程（即，让协程向前执行到第一个yield表达式，准备好作为活跃的协程使用）。

## 使用协程计算移动平均值
```python
def averager():
    total = 0.0
    count = 0
    average = None
    
    while True:
        item = yield average
        total += item
        count += 1
        average = total / count

a = averager()
next(a)
a.send(10) # 10.0
a.send(30) # 20.0
```

## 预激协程的装饰器
```python
from functools import wraps
def coroutine(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer

@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    
    while True:
        item = yield average
        print(item, total, count, average)
        total += item
        count += 1
        average = total / count

a = averager()
# next(a) 不再需要
a.send(10)
```

