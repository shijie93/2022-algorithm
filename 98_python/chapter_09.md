# 符合Python风格的对象

## classmethod与staticmethod

classmethod 用来操作类，staticmethod 只是定义在类中的普通方法。

## Python的私有属性和“受保护的”属性
Python 不能像 Java 那样使用private 修饰符创建私有属性，但是Python 有个简单的机制，能避免子类意外覆盖“私有”属性。举个例子。有人编写了一个名为Dog的类，这个类的内部用到了mood 实例属性，但是没有将其开放。现在，你创建了Dog类的子类：Beagle。如果你在毫不知情的情况下又创建了名为mood的实例属性，那么在继承的方法中就会把 Dog类的mood 属性覆盖掉。这是个难以调试的问题。为了避免这种情况，如果以 `__mood`的形式（两个前导下划线，尾部没有或最多有一个下划线）命名实例属性，Python 会把属性名存入实例的`__dict__` 属性中，而且会在前面加上一个下划线和类名。因此，对 Dog类来说，`__mood`会变成 `_Dog__mood`；对 Beagle类来说，会变成 `_Beagle__mood`。这个语言特性叫名称改写（name mangling）。

名称改写是一种安全措施，不能保证万无一失：它的目的是避免意外访问，不能防止故意做错事。Python解释器不会对使用单个下划线的属性名做特殊处理，不过这是很多 Python 程序员严格遵守的约定，他们不会在类外部访问这种属性。 遵守使用一个下划线标记对象的私有属性很容易，就像遵守使用全大写字母编写常量那样容易。

## `__slots__`

`__slots__`的问题总之，如果使用得当，`__slots__` 能显著节省内存，不过有几点要注意。
* 每个子类都要定义 _`_slots__` 属性，因为解释器会忽略继承的`__slots__` 属性。
* 实例只能拥有`__slots__`中列出的属性，除非把 '`__dict__`' 加入 `__slots__`中（这样做就失去了节省内存的功效）。
* 如果不把 '_`_weakref__`' 加入 `__slots__`，实例就不能作为弱引用的目标。

如果你的程序不用处理数百万个实例，或许不值得费劲去创建不寻常的类，诸如其实例可能不接受动态属性或不支持弱引用。与其他优化措施一样，仅当权衡当下的需求并仔细搜集资料后证明确实有必要时，才应该使用__slots__ 属性。

## 实例覆盖类属性
Python 有个很独特的特性：类属性可用于为实例属性提供默认值。但是，**如果为不存在的实例属性赋值，会新建实例属性**。 以下例子可充分说明：

```python
class Vector:
    typecode = 'd'

v = Vector()

assert v.typecode == Vector.typecode
assert v.typecode is Vector.typecode
print(v.__dict__)

v.typecode = 'i'
assert v.typecode != Vector.typecode
assert v.typecode is not Vector.typecode
print(v.__dict__)
```

输出如下：
```
{}
{'typecode': 'i'}
```

当为不存在的实例属性赋值时，会新建实例属性，但类属性保持不变。

