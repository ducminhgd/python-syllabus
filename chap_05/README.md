# Các kiểu dữ liệu (Nâng cao)

## Chuỗi (string)

Python là một trong các ngôn ngữ rất mạnh về việc xử lý chuỗi, gần như các hàm built-in của chuỗi trong Python có thể xử lý được tất cả các nhu cầu của người sử dụng.

Đọc thêm tại: https://www.w3schools.com/python/python_ref_string.asp

Ngoài ra, Python rất mạnh trong việc format chuỗi mà các ngôn ngữ khác chưa hỗ trợ nhiều.

Ví dụ:

```python
my_name = 'Minh'
hello_1 = f'Hello, {my_name}'
hello_2 = 'Hello, {name}'.format(name=my_name)
hello_3 = 'Hello, {}'.format(my_name)
```

Trong ví dụ trên, có một phương pháp được sử dụng gọi là **f-strings**.

Đọc thêm về hướng dẫn sử dụng cho những trường hợp nâng cao:
- https://zetcode.com/python/fstring/
- [Format code](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes)

## Ngày giờ

Đọc thêm:
- https://docs.python.org/3/library/datetime.html
- https://www.w3schools.com/python/python_datetime.asp

### Các kiểu trong module `datetime`

- `datetime.date`: ngày, có các thuộc tính `year`, `month`, `day`.
- `datetime.time`: giờ, có các thuộc tính `hour`, `minute`, `second`, `microsecond`, `tzinfo`.
- `datetime.datetime`: kết hợp của `datetime.date` và `datetime.time`.
- `datetime.timedelta`: thời lượng của sự khác nhau giữa 2 đối tượng kiểu `date`, kiểu `time` hoặc kiểu `datetime`.
- `datetime.tzinfo`: abstract base class cho Timezone.
- `datetime.timezone`: class được implement cho `tzinfo` với offset được set là UTC.

Mối quan hệ giữ các class

```
object
    timedelta
    tzinfo
        timezone
    time
    date
        datetime
```

### Naive và Aware

Naive: không giữ thông tin timezone (`tzinfo`)
Aware: thông tin ngày/giờ có timezone được xác định.

Các đối tượng thuộc lớp `date` luôn là naive.

Các đối tượng thuộc lớp `time` có thể là naive hoặc aware -> các đối tượng ccủa `datetime` cũng có thể là naive hoặc aware.

Một đối tượng `t` thuộc lớp `time` là aware khi và chỉ khi thỏa 2 điều kiện sau:
- `t.tzinfo` không phải `None`.
- `t.tzinfo.utcoffset(None)` không trả về `None`.
Ngược lại, `t` là naive.

Một đối tượng `d` thuộc lớp `datetime` là aware khi và chỉ khi thỏa 2 điều kiện sau:
- `d.tzinfo` không phải `None`.
- `d.tzinfo.utcoffset(d)` không trả về `None`.
Ngược lại, `d` là naive.

### Các thao tác thường sử dụng với Datetime

1. Lấy ngày giờ hiện tại

  ```python
  import datetime

  datetime_object = datetime.datetime.now()
  print(datetime_object)

  date_object = datetime.date.today()
  print(date_object)
  ```

1. Khởi tạo các object

  ```python
  from datetime import time

  # time(hour = 0, minute = 0, second = 0)
  a = time()
  print("a =", a)

  # time(hour, minute and second)
  b = time(11, 34, 56)
  print("b =", b)

  # time(hour, minute and second)
  c = time(hour = 11, minute = 34, second = 56)
  print("c =", c)

  # time(hour, minute, second, microsecond)
  d = time(11, 34, 56, 234566)
  print("d =", d)
  ```

1. Tính thời lượng khác nhau giữa 2 thời điểm

  ```python
  from datetime import datetime, date

  t1 = date(year = 2018, month = 7, day = 12)
  t2 = date(year = 2017, month = 12, day = 23)
  t3 = t1 - t2
  print("t3 =", t3)

  t4 = datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
  t5 = datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 55, second = 13)
  t6 = t4 - t5
  print("t6 =", t6)

  print("type of t3 =", type(t3)) 
  print("type of t6 =", type(t6))  
  ```

1. "Khoảng cách" giữa 2 object `timedelta`

  ```python
  from datetime import timedelta

  t1 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
  t2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
  t3 = t1 - t2

  print("t3 =", t3)
  ```

1. Format ngày giờ theo định dạng, sử dụng `strftime()` (string from time)

  ```python
  from datetime import datetime

  # current date and time
  now = datetime.now()

  t = now.strftime("%H:%M:%S")
  print("time:", t)

  s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
  # mm/dd/YY H:M:S format
  print("s1:", s1)

  s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
  # dd/mm/YY H:M:S format
  print("s2:", s2)
  ```

1. Tạo object ngày giờ từ chuỗi có sẵn, sử dụng `strptime()` (String parsed to time)

  ```python
  from datetime import datetime

  date_string = "21 June, 2018"
  print("date_string =", date_string)

  date_object = datetime.strptime(date_string, "%d %B, %Y")
  print("date_object =", date_object)
  ```

1. Xử lý timezone, có dùng package `pytz`

  ```python
  from datetime import datetime
  import pytz

  local = datetime.now()
  print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))


  tz_NY = pytz.timezone('America/New_York') 
  datetime_NY = datetime.now(tz_NY)
  print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))

  tz_London = pytz.timezone('Europe/London')
  datetime_London = datetime.now(tz_London)
  print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))
  ```

## Enum

Enum, hay Enumeration, là thường dùng để định nghĩa một số các giá trị cố định. Trong Python không có `const` thật sự, nên Enum là một giải pháp cho vấn đề này.

```python
import enum

MY_CONST = 3
MY_CONST = 4 # OK

class MyEnum(enum.Enum):
  NAME = 'NAME'

MyEnum.NAME = 'NAME2' # AttributeError: Cannot reassign members.
```

[Các thuộc tính/class của module `enum`](https://docs.python.org/3/library/enum.html#module-contents)

Đặc biệt hàm `auto()` gán giá trị cho các thuộc tính của Enum tăng dần, bắt đầu từ `1`.

## Mutable và immutable

Mutable có nghĩa là "thay đổi được", immutable là "không thay đổi được".

Cho ví dụ sau:

```python
def add(l: list, n: int) -> list:
    for i in range(0, len(l)):
        l[i] = l[i] + n
    return l


a = [1, 2]
b = add(a, 3)
print(b) # [4, 5]
print(a) # [4, 5]
c = add(b, 3)
print(a) # [7, 8]
```

và

```python
class MyClass:
    my_attr = {}


a = MyClass()
a.my_attr = {1, 2, 3, 4}
b = MyClass()
print(b.my_attr)  # {}
MyClass.my_attr = {1, 2, 3, 4}
c = MyClass() # {1, 2, 3, 4}
print(c.my_attr)
```

List `l` đã bị thay đổi bởi hàm `add`.

Các kiểu dữ liệu Mutable bao gồm: 

- Lists
- Sets
- Dictionaries
- User-Defined Classes (tùy thuộc vào các người dùng định nghĩa class) 

Các kiểu dữ liệu Immutable gồm: 

- Numbers (Integer, Rational, Float, Decimal, Complex & Booleans)
- Strings
- Tuples
- Frozen Sets
- User-Defined Classes (tùy thuộc vào các người dùng định nghĩa class)

Có thể tạm hiểu là đối với các kiểu dữ liệu Mutable thì khi truyền vào hàm thì truyền dạng tham chiếu (biến giữ địa chỉ chứ không phải giá trị). Do đó, các hàm sử dụng tham số dạng tùy chọn (optional) thì không nên cho giá trị default là các kiểu dữ liệu Mutable.

Có nhiều cách để tránh trường hợp này là dùng `deepcopy`.

Đọc thêm: https://www.mygreatlearning.com/blog/understanding-mutable-and-immutable-in-python/


## Bài tập

1. Cho số tự nhiên `n`, in ra hình vuông `n x n` bằng ký tự `*`. Ví dụ n=3

    ```
    * * *
    * * *
    * * *
    ```

2. Cho số tự nhiên `n`, in ra hình tam giác cân với 2 cạnh bên bằng `n` ký tự `*`. Ví dụ: n=5

    ```
    *
    * *
    * * *
    * * * *
    * * * * *
    ```

    hoặc

    ```
            *
          * * *
        * * * * *
      * * * * * * *
    * * * * * * * * *
    ```

    hoặc bất cứ hình dạng nào mà đáp ứng được yêu cầu.

3. Cho 2 số tự nhiên `a` và `b`, vẽ hình chữ nhật rỗng a x b.

    ```
    ****************************
    *                          *
    *                          *
    *                          *
    ****************************
    ```