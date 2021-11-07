# Chương 2

## Hello World

1. Tạo một file python `hello.py` có nội dung như sau

    ```python
    print("Hello world!")
    ```

    Chạy lệnh `python hello.py` để xem kết quả.

1. Cập nhật lại file `hello.py` với nội dung sau

    ```python
    if __name__ == '__main__':
        print("Hello world!")
    ```

    Chạy lệnh `python hello.py` để xem kết quả.

## `__name__`

1. Tạo ra 2 file `main.py` và `notmain.py` với nội dung như sau:

    ```python
    # notmain.py
    print('__name__ is ' + __name__)

    if __name__ == '__main__':
        print('__name__ is __main__')
    ```

    ```python
    # main.py
    import notmain

    if __name__ == '__main__':
        print('This is main.py')
    ```

1. Chạy 2 lệnh như sau và xem kết quả:

    - `python notmain.py`

        ```bash
        ➜ python notmain.py 
        __name__ is __main__
        __name__ is __main__
        ```

    - `python main.py`

        ```bash
        ➜ python main.py   
        __name__ is notmain
        This is main.py
        ```
    
    `__name__` được đại diện cho module hiện tại. Trong trường hợp module/file được chạy sau lệnh `python` thì mặc định biến `__name__` mang giá trị là `__main__`.

Thông thường, dòng lệnh `if __name__ == '__main__':` được dùng để ràng buộc việc module được import sẽ không chạy những câu lệnh không nên chạy.

## Package & Module

Trong Python, một file có tên `x.py` là thể hiện, nội dung của module `x`. Tập hợp các module được gọi là Package. Đối với Python phiên bản 3.2 trở về trước, một package phải bao gồm một file `__init__.py`.

Ví dụ:

```bash
.
├── snippets
│   ├── __init__.py
│   ├── main.py
│   ├── notmain.py
```

Thì khi dùng câu lệnh `import snippets` mới được hiệu quả đối với Python 3.2 trở về trước, nếu không phải sử dụng `from snippets import main, notmain`.

## Một số kiểu dữ liệu cơ bản

Python là ngôn ngữ có kiểu dữ liệu động, nên mỗi khi biến được khởi tạo với giá trị kiểu gì thì nó sẽ kiểu dữ liệu của giá trị đó.

Các kiểu dữ liệu có sẵn của Python

| Kiểu              | Mô tả                                                                                                                                             |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bool`            | Kiểu logic                                                                                                                                        |
| `int`             | Số nguyên                                                                                                                                         |
| `float`           | Số chấm động                                                                                                                                      |
| `decimal.Decimal` | Số thập phân                                                                                                                                      |
| `str` (string)    | Chuỗi ký tự                                                                                                                                       |
| `list`            | Danh sách, tương ứng với mảng của một số ngôn ngữ khác                                                                                            |
| `tuple`           | Cũng giống `list`. Khác `list` là tuple `immutable`                                                                                               |
| `set`             | Cũng giống `list`. Khác `list` ở 2 điểm chính là set `immutable` và các phần tử là duy nhất.                                                      |
| `dictionary`      | Các phần tử bao gồm 2 phần: key và value. Key tồn tại duy nhất và không trùng với key khác. Giống Hash Table hoặc Hash Map ở một số ngôn ngữ khác |

Đối với `list`, `set`, `tuple`, vị trí của các phần tử được chạy từ `0` đến `n-1`, với `n` là tổng số phần tử trong `list`, `set`, `tuple`. Để truy cập phần tử thứ `k` của `list`/`set`/`tuple` `a` thì ta dùng `a[k-1]`.

Đối với `dictionary`, để truy cập một phần tử thì ta dùng `d[key]`, với `key` là một khóa được tồn tại trong `d`.

```python
from decimal import Decimal

right = True
wrong = False

my_int = 1
my_float = 0.1
my_decimal = Decimal('0.1')
my_str = 'Hello my friend'

my_list = [42, 42, 42, 42]
print(my_list[1])
my_list2 = [42, 'string', 0.1]

my_tuple = (42, 42,)
print(my_tuple[1])
my_tuple = 42, 42,
print(my_tuple[1])
my_tuple2 = (42, 'string',)
print(my_tuple2[1])
my_tuple3 = tuple(my_tuple2)

my_set = set([42, 42, 42, 42])
print(my_set[0])
my_set2 = set(my_list)

my_dict = {'key': 'value', 'key2': 'value2'}
print(my_dict['key2'])
print(my_dict['key3']) # error
print(my_dict.get('key3'))
print(my_dict.get('key3', 'Không tồn tại'))
```

## Function

Các hàm trong Python được khai báo với định dạng

```python
def say_hello():
    print('Hello')

def say_hello2(name: str):
    print('Hello, ' + name)

def sum_int(a: int, b: int) -> int:
    return a + b
```

## Bài tập

1. Tạo ra các hàm sau: tính cộng, trừ, nhân, chia các số nguyên.
1. Viết function khi nhập vào một biến thì trả ra kiểu dữ liệu của biến đó.