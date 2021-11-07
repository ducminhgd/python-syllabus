# Toán tử và Cấu trúc điều khiển

## Các toán tử

### Toán tử toán học

| Toán tử | Diễn giải               |
| ------- | ----------------------- |
| `+`     | Cộng                    |
| `-`     | Trừ                     |
| `*`     | Nhân                    |
| `**`    | Lũy thừa                |
| `/`     | Chia                    |
| `%`     | Chia lấy số dư (modulo) |
| `//`    | Chia lấy Phần nguyên    |

```python
print(5 + 2) # 7
print(5 - 2) # 3
print(5 * 2) # 10
print(5 ** 2) # 25
print(5 / 2) # 2.5
print(5 % 2) # 1
print(5 // 2) # 2
print("Minh" * 5) # MinhMinhMinhMinhMinh
print([42] * 3) # [42, 42, 42]
```

### Toán tử gán

Thực hiện phép toán rồi gán lại giá trị mới

| Toán tử | Diễn giải               |
| ------- | ----------------------- |
| `+=`    | Cộng                    |
| `-=`    | Trừ                     |
| `*=`    | Nhân                    |
| `**=`   | Lũy thừa                |
| `/=`    | Chia                    |
| `%=`    | Chia lấy số dư (modulo) |
| `//=`   | Chia lấy Phần nguyên    |

```python
a = 1
print(a) # 1
a += 2
print(a) # 3
```

### Toán tử so sánh

| Toán tử | Diễn giải          |
| ------- | ------------------ |
| `==`    | So sánh bằng       |
| `!=`    | So sánh không bằng |
| `>`     | Lớn hơn            |
| `<`     | Nhỏ hơn            |
| `>=`    | Lớn hơn hoặc bằng  |
| `<=`    | Nhỏ hơn hoặc bằng  |

```python
print(1 == 1) # True
print(1 == 2) # False
print(1 != 2) # True
print(1 < 2) # True
print(1 <= 2) # True
print(1 > 2) # False
print(1 >= 2) # False
print(1 == "1") # True
print(1 == "2") # False
print(1 != "2") # True
print(1 < "2") # TypeError: '<' not supported between instances of 'int' and 'str'
print(1 <= "2") # TypeError: '<=' not supported between instances of 'int' and 'str'
print(1 > "2") # TypeError: '>' not supported between instances of 'int' and 'str'
print(1 >= "2") # TypeError: '>=' not supported between instances of 'int' and 'str'
```

### Toán tử logic

| a     | b     | a `and` b | a `or` b | `not` a |
| ----- | ----- | --------- | -------- | ------- |
| True  | True  | True      | True     | False   |
| True  | False | False     | True     | False   |
| False | True  | False     | True     | True    |
| False | False | False     | False    | True    |

### Toán tử định danh
| Toán tử | Diễn giải                                                         |
| ------- | ------------------------------------------------------------------|
| `is`    | `True` nếu 2 đối tượng cùng 1 địa chỉ vùng nhớ và ngược lại       |
| `is not`| `True` nếu 2 đối tượng không cùng 1 địa chỉ vùng nhớ và ngược lại |

```python
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)  # True
print(x is y)  # False
```

### Toán tử quan hệ
| Toán tử | Diễn giải                                                     |
| ------- | --------------------------------------------------------------|
| `in`    | `True` nếu một đối tượng `thuộc 1 tập hợp` và ngược lại       |
| `not in`| `True` nếu một đối tượng `không thuộc 1 tập hợp` và ngược lại |

```python
x = ["apple", "banana"]

print("banana" in x) # True
print("mango" not in x) # True
```
### Toán tử bitwise
| Toán tử | Diễn giải            |
| ------- | ---------------------|
| `&`     | AND                  |
| `|`     | OR                   |
| `^`     | XOR                  |
| `~`     | NOT                  |
| `<<`    | Dịch sang trái 1 bit |
|  `>>`   | Dịch sang phải 1 bit |

```python
   a = 3 # 00000011
   b = 1 # 00000001
   print(a & b)  # 00000011 & 00000001 = 00000001 = 1
   print(a | b)  # 00000011 | 00000001 = 00000011 = 3
   print(a ^ b)  # 00000011 ^ 00000001 = 00000010 = 2
   print(~b)     # ~00000001           = 11111110 = -2
   print(a << 1) # 000000011 << 1      = 00000110 = 6
   print(a >> 1) # 000000011 >> 1      = 00000001 = 1
```
### Thứ tự thực hiện

| Thứ tự | Toán tử                                        |
| ------ | -----------------------------------------------|
| 1      | `**`                                           |
| 2      | `~x`                                           |
| 3      | `+x, -x`                                       |
| 4      |  `*`, `/`, `%`, `//`                           |
| 5      | `+`, `-`                                       |
| 6      | `<<, >>`                                       |
| 7      | `&`                                            |
| 8      | `^`                                            |
| 9      | `|`                                            |
| 10     | Các toán tử so sánh                            |
| 11     | Các toán tử gán                                |
| 12     | Các toán tử định danh, quan hệ, logic          |


## Cấu trúc điều khiển
### Cấu trúc `if/elif/else`
     
```python
num = 10
if num <= 5:
    print("Bad")
elif num <= 8:
    print("Normal")
else:
    print("Good")

```
### Cấu trúc lặp `while`

https://realpython.com/python-while-loop/#the-while-loop

Cú pháp

    ```python
    while <expr>:
        <statement(s)>
    ```

Diễn giải: trong khi `<expr>` còn đúng thì thực hiện các câu lệnh `<statement(s)>`. Ví dụ:

1. Đơn giản

    ```python
    i = 0
    while i < 5:
        print(i)
        i = i + 1
    ```

    Kết quả
    ```bash
    0
    1
    2
    3
    4
    ```

2. Lặp với 2 điều kiện

    ```python
    i, j = 0, 0
    while i < 5 and j < 2:
        print(i)
        i = i + 1
        j += 1
    ```

    Kết quả
    ```
    0
    1
    2
    ```

3. Lặp với mảng

    ```python
    a = ['H', 'E', 'L', 'L', 'O']
    while a:
        print(a.pop(0))

    # H
    # E
    # L
    # L
    # O
    ```

Nếu muốn vòng lặp, lặp vô tận thì có thể dùng `while True` hoặc `while 1`.

#### `break` và `continue`

- `break` dùng để thoát ra khỏi vòng lặp `while`

- `continue` dùng để bỏ qua bước lặp.

```python
i = 0
while i < 5:
    i = i + 1
    if i == 3:
        break
    print(i)

# 1
# 2
```

```python
i = 0
while i < 5:
    i = i + 1
    if i % 2:
        continue
    print(i)

# 2
# 4
```

#### `while` với `else`

```python
while <expr>:
    <statement(s)>
else:
    <additional_statement(s)>
```

Ví dụ:

```python
a = ['H', 'E', 'L', 'L', 'O']
while a:
    c = a.pop(0)
    if c == 'L':
        break
    print(c)
else:
    print("Done")

# H
# E
```

`else` được thực hiện khi điều kiện `<expr>` không còn đúng nữa. Ở ví dụ trên thì vòng lặp bị `break` trong khi điều kiện `<expr>` vẫn còn đúng, nên `print("Done")` không được thực hiện.

Ứng dụng khác:

```python
a = [1, 3, 5, 7]
while a:
    c = a.pop(0)
    if c % 2 == 0:
        result = c
        break
else:
    result = 0
print(result)

# 0
```

### Cấu trúc lặp `for`

Cú pháp:

```python
for <var> in <iterable>:
    <statement(s)>
```

#### Chi tiết các cách sử dụng

1. Lặp theo số bước lặp
    
    ```python
    for i = 1 to 10
        <loop body>
    ```

2. Lặp theo số bước lặp, rõ ràng.

    ```python
    for (i = 1; i <= 10; i++)
        <loop body>
    ```

3. Lặp theo "bộ lặp"

    ```python
    for i in <collection>
        <loop body>
    ```

    ```python
    s = 'Hello!'
    for c in s:
        print(c)
    ```

    ```python
    for n in (0, 1, 2, 3, 4):
        print(n)
    ```

4. Lặp Dictionary

    ```python
    d = {
        'k1': 'v1',
        'k2': 'v2',
        'k3': 'v3',
    }
    for i in d:
        print(i)
    for i in d.items():
        print(i)
    for k, v in d.items():
        print(v)
    for i in d.keys():
        print(i)
    for i in d.values():
        print(i)
    ```
5. Lặp với range
    ```python
    for i in range(0, 10):
        print(i)
    ```
6. Lặp với range kèm số bước nhảy:
    ```python
    for i in range(0, 10, 2): # 2 là số bước nhảy
        print(i)
    ```
#### `else`

Giống như `while`.

### `match` 
(Tương tự như `switch` của các ngôn ngữ khác)

```python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 401 | 403:
            return "Permission Denied"
        case _:
            return "Something's wrong with the internet"
print(http_error(400)) # Bad request
```
## Bài tập

1. Cấu trúc điều khiển
   1. Cho số nguyên dương n, viết hàm tính tổng $S(n) = 1 + 2 + 3 + .... + n$.

        ```python
        def sn(n: int) -> int:
            result = 0
            for i in range(0, n + 1):
                result += i
            return result

        if __name__ == '__main__':
            print(sn(3))
        ```

   2. Cho số nguyên dương n, viết hàm tính $`S(n) = 1 + 3 + 5 + ... + (2n + 1)`$
   3. Cho số nguyên dương n, viết hàm tính $`S(n) = 1 + 2^2 + 3^3 + ... + n^n`$
   4. Cho số nguyên dương n, viết hàm tính $`S(n) = 1 + 1/2 + 1/3 + ... + 1/n`$
   5. Cho số nguyên dương n, viết hàm tính $`S(n) = 1 * 2 * 4 * ... * 2n`$
   6. Cho số nguyên dương n, viết hàm tính $`fibo(n) = 1 + 2 + 3 + 5 + 8 + ... + f(n-1)`$
   7. Cho số nguyên dương n và số nguyên k, viết hàm tính $`S(n) = 1 + 2 + ... + n`$, sao cho S(n) < k.
   8. Số chính phương là số nguyên và là bình phương của một số khác, hãy viết hàm kiểm tra n có phải ls61 số chính phương hay không?
   9. Số nguyên tốt là số có hai thương số duy nhất là 1 và chính nó. Hãy viết hàm kiểm tra xem n có phải là số nguyên tốt hay không?
   10. Năm nhuận là năm chia hết cho 4 và không chia hết cho 100, hãy viết hàm kiểm tra năm n có phải là năm nhuận hay không?
   11. Viết hàm đến từ năm n đến năm m có bao nhiêu năm nhuận.
2. List và Tuple
   1. Cho một list/tuple số nguyên `a`, viết hàm in ra các giá trị chẵn của `a`.
   2. Cho một list/tuple số nguyên `a`, viết hàm tính tổng các số lẻ của `a`.
   3. Cho một list/tuple số nguyên `a` và số nguyên `n`, viết hàm đến số lần xuất hiện của `n` trong `a`.
   4. Cho một list/tuple số nguyên `a`, viết hàm đếm số lượng số nguyên tố trong `a`.