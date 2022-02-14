# 上下文管理器和else 块

else 子句不仅能在if语句中使用，还能在for、while和try语句中使用。

**for**

仅当 for 循环运行完毕时（即 for 循环没有被break语句中止）才运行 else 块。

**while**

仅当 while 循环因为条件为假值 而退出时（即 while 循环没有被break语句中止）才运行 else 块。

**try**

仅当 try 块中没有异常抛出时才运行 else 块。官方文档还指出：“else 子句抛出的异常不会由前面的except 子句处理。”

在所有情况下，如果异常或者 return、break或continue语句导致控制权跳到了复合语句的主块之外，else 子句也会被跳过。

```python
    try:
        dangerous_call()
    except OSError:
        log('OSError...')
    else:
        after_call()
```
try 块防守的是dangerous_call() 可能出现的错误，而不是after_call()。而且很明显，只有try 块不抛出异常，才会执行 after_call()。

## 上下文管理器和with块

上下文管理器协议包含 `__enter__`和 `__exit__` 两个方法。with语句开始运行时，会在上下文管理器对象上调用 `__enter__` 方法。with语句运行结束后，会在上下文管理器对象上调用 `__exit__` 方法，以此扮演 finally 子句的角色。

```python
with open('data.bin', 'rb') as fp:
    src = fp.read(60)
```
不管控制流程以哪种方式退出 with 块，都会在上下文管理器对象上调用 `__exit__` 方法，而不是在 `__enter__` 方法返回的对象上调用。

> 重要：with 并没有定义新的作用域

## contextmanager 上下文管理器

```python
import contextlib

@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write
    
    def reverse_write(text):
        original_write(text[::-1])
    
    sys.stdout.write = reverse_write
    msg = ""
    try:
        yield 'JABBERWOCKY'
    except ZeroDivisionError:
        msg = 'Please DO NOT divide by zero!'
    finally:
        sys.stdout.write = original_write
    if msg:
        print(msg)

with looking_glass() as what:
    print('Alice, Kitty and Snowdrop')
    print(what)

with looking_glass() as what:
    a = 1 / 0
    print('Alice, Kitty and Snowdrop')
    print(what)
```
输出如下：
```
pordwonS dna yttiK ,ecilA
YKCOWREBBAJ
Please DO NOT divide by zero!
```