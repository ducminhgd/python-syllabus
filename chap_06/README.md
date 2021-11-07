# Hướng đối tượng với Python

Lập trình hướng đối tượng (hay Object Oriented Programming), có 4 nguyên lý sau:

- Tính đóng gói (Encapsulation): Các dữ liệu và phương thức có liên quan với nhau được đóng gói thành 1 lớp. Tức là mỗi lớp được xây dựng để thực hiện một nhóm chức năng đặc trưng của riêng lớp đó. Che giấu các thông tin của lớp đó đối với bên ngoài thể hiện ở *public*, *protected*, *private* đối với từng thuộc tính và phương thức.
- Tính kế thừa (Inheritance): Nguyên tắc này cho phép xây dựng một lớp mới dựa trên 1 lớp đã khai báo từ trước. Lớp con có thể sử dụng lại các thuộc tính và phương thức của lớp cha mà không cần khai báo lại. Tùy thuộc vào từng ngôn ngữ cho phép việc kế thừa 1 hoặc nhiều class cha.
- Tính trừu tượng (Abstraction): tổng quát hóa phương thức của đối tượng không quan tâm phương thức thực hiện như thế nào, được thể hiện bởi interface (có các tên phương thức nhưng ko có body của phương thức, khi class nào implement interface thì thực hiện nó).
- Tính đa hình (Polymorphism): Tính đa hình được thể hiện bởi một phương thức, hành động có thể thực hiện theo nhiều cách khác nhau. VD: chó mèo cùng là động vật nhưng khi thực hiện phương thức *kêu* thì chó sủa *gâu gâu*, mèo thì *meo meo*.

Riêng đối với Python:
- Tính đóng gói không rõ ràng vì không phân biệt scope.
- Tính trừu tượng thường không cần thiết sử dụng.

Các hàm trong hướng đối tượng thường được gọi là *phương thức* (Method).

## Scope (phạm vi) trong hướng đối tượng

- Private: chỉ được truy cập và sử dụng bởi đối tượng thuộc lớp đó.
- Protected: chỉ được truy cập và sử dụng bởi đối tượng thuộc lớp đó hoặc lớp con.
- Public: không giới hạn, được sử dụng rộng rãi.

## Class (lớp) và Instance/Object (đối tượng)

Trong hướng đối tượng thì các "đơn vị" trong cuộc sống thực được *trừu tượng hóa* thành các Object hay Instance. Để tái sử dụng các thuộc tính (attribute) của các đối tượng, thì thông tin chung của các đối tượng được định nghĩa trong một khuôn mẫu gọi là *Class*.

```python
class Animal:
    name: str = None
    weight: float = None

    def __init__(self, name, weight=None):
        self.name = name
        if weight is not None:
            self.weight = weight

    def speak(self):
        if bool(self.name):
            print(f"I'm {self.name}, an animal")
        else:
            print("I'm an animal")

    def __private_func(self):
        print("Animal")

    def _protected_func(self):
        print("Protected function of Animal class")

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.name}, {self.weight}"


class Lion(Animal):
    def __init__(self, name, weight=None):
        super().__init__(name, weight)

    def speak(self):
        if bool(self.name):
            print(f"I'm {self.name}, a lion")
        else:
            print("I'm an lion")


class Tiger(Animal):
    def speak(self):
        if bool(self.name):
            print(f"I'm {self.name}, a tiger")
        else:
            print("I'm an tiger")


class Liger(Lion, Tiger):
    """Liger is a real animal
    """

    def __init__(self, name, weight=None):
        super().__init__(name, weight)


animal = Animal("Animal name")
lion = Lion("Simba", 100)
tiger = Tiger("Kitten", 101)
liger = Liger("Liger")

print(animal)  # Animal: Animal name, None
# animal.__private_func()  # AttributeError: 'Animal' object has no attribute '__private_func'
animal._protected_func()  # Protected function of Animal class
animal.speak() # I'm Animal name, an animal
print("--------------------------------")

print(lion) # Lion: Simba, 100
lion.speak() # I'm Simba, a lion
lion._protected_func()  # Protected function of Animal class
print("--------------------------------")

print(tiger) # Tiger: Kitten, 101
tiger.speak() # I'm Kitten, a tiger
print("--------------------------------")

print(liger) # Liger: Liger, None
liger.speak() # I'm Liger, a lion
liger._protected_func()  # Protected function of Animal class
```

### Tính đóng gói

Trong Python thì tính đóng gói không được thể hiện rõ ràng, mà chỉ mang tính *quy ước* theo cú pháp.
- Tên biến, hàm bắt đầu bằng `__` là private.
- Tên biến, hàm bắt đầu bằng `_` là protected.
- Còn lại là public.

### Tính kế thừa

Mọi class trong Python đều kế thừa từ `object`, nên `class Animal:` chính là `class Animal(object):`.

Python là một ngôn ngữ đa thừa kế, ví dụ lớp `Liger` kế thừa từ `Lion` và `Tiger`; `Lion` và `Tiger` kế thừa từ `Animal`. Trong trường hợp các thuộc tính hoặc phương thức trùng nhau thì sẽ ưu tiên sử dụng theo thứ tự từ trái sang phải. Ví dụ như class `Liger`.

### Tính trừu tượng

```python
from abc import ABC, abstractmethod


class AbstractClassExample(ABC):

    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod
    def do_something(self):
        pass

class ChildExample(AbstractClassExample):
    ...

example = AbstractClassExample() # TypeError: Can't instantiate abstract class AbstractClassExample with abstract methods do_something
child_example = ChildExample() # TypeError: Can't instantiate abstract class ChildExample with abstract methods do_something
```

### Tính đa hình

Dự vào ví dụ trên là phương thức `def speak(self)`

## Class method và static method

Class method có thể sử dụng và thay đổi thuộc tính của class; Static method thì không.

```python
class MyClass:
    my_int = 0

    @classmethod
    def print_int(cls):
        print(cls.my_int)
        cls.my_int = 42
        print(cls.my_int)

    @staticmethod
    def my_static():
        print('my_static')

MyClass.print_int()
MyClass.print_int()
MyClass.my_static()

# 0
# 42
# 42
# 42
# my_static
```

## Class attribute và Instance attribute

Class attribute thì có thể được sử dụng hoặc thay đổi theo class, những Instance được tạo từ class sau khi thay đổi cũng ảnh hưởng theo.

```python
class MyClass:
    my_int = 0
    my_list = []

    def set_int(self, i: int):
        self.my_int = i

    def add_list(self, x: int):
        self.my_list.append(x)


a = MyClass()
print(a.my_int) # 0
a.my_int = 4
print(a.my_int) # 4
print(a.my_list) # []
a.add_list(1)
a.add_list(2)
print(a.my_list) # [1, 2]

b = MyClass() 
print(b.my_list) # [1, 2]
print(b.my_int) # 4

MyClass.my_int = 42
c = MyClass()
print(c.my_int) # 42
```

-> Attribute của class nên là các kiểu immutable và nên có hàm constructure init giá trị ban đầu cho các instance được tạo ra, tránh bị override.

## Functional Programming

Python là ngôn ngữ vừa là OOP vừa là FP.

Functional Programming là cách lập trình hàm, sử dụng các hàm như toán học `f(x)`, `g(x)`, `f(g(x))`. Có thể hiểu nôm na thì trong Functional Programming thì mọi đối tượng đều làm hàm.

Functional Programming hướng đến tính kết hợp (composability) các hàm (function) để tối đa hóa khả năng tái sử dụng (reusability) trong chương trình.

Các đặc tính rõ nhất của Functional Programming là:
1. Pure function: hàm không có tính năng thay đổi input.
2. Hàm luôn trả về kết quả.
3. Những gì đã khai báo thì không được thay đổi, immutable.

```python
x = 'Minh'

def to_lower(x: str) -> str:
    return x.lower()

def to_upper(x: str) -> str:
    return x.upper()

print(to_upper(to_lower(x)))
```