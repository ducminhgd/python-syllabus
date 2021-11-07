# Input/Output

## Đọc từ Command line và in ra console

Đọc từ command line sử dụng hàm `input`, ví dụ: `input("Nhập số a: ")`.

In ra console có nhiều cách sử dụng, trong đó đơn giản nhất là dùng hàm `print`, ví dụ: `print('Hello world')`.

## Đọc và ghi file.

Cú pháp

```python
file_handler = open('path/to/file', <mode>)
```

Trong đó, `mode` gồm:
- `r`: đọc file (read)
- `rb`: đọc file nhị phân (binary read)
- `w`: ghi file (write)
- `wb`: ghi file nhị phân (binary write)
- `a`: ghi nối và nội dung file (append)

Thông thường, khi file được mở với quyền edit (`w`, `wb`, `a`) thì file sẽ bị khóa lại. Hai process khác nhau khi truy cập một file thì process nào đến trước sẽ được làm trước. File chỉ được mở khóa khi được gọi hàm `close()` hoặc kết thúc process.

Các hàm đọc file text:

- Đọc toàn bộ nội dung file
  
    ```python
    fh = open(file_path, 'r')
    content = fh.read()
    fh.close()
    ```

- Đọc một dòng

    ```python
    fh = open(file_path, 'r')
    line = fh.readline()
    fh.close()
    ```

- Đọc toàn bộ file vào mảng các dòng

    ```python
    fh = open(file_path, 'r')
    lines = fh.readlines()
    fh.close()
    ```

- Đọc từng dòng theo dạng iterator, thích hợp cho việc đọc file quá lớn

    ```python
    fh = open(file_path, 'r')
    for line in fh:
        print(line)
    fh.close()
    ```

- Ghi một dòng

    ```python
    fh = open(file_path, 'r')
    fh.write('Hello')
    fh.close()
    ```

- Ghi nhiều dòng

    ```python
    fh = open(file_path, 'r')
    fh.writelines('Hello', 'world')
    fh.close()
    ```

- Đọc ghi trong context

    ```python
    with open(file_path, 'r') as fh:
        print(fh.readline())
    ```

    với `with <context>` thì những gì trong context đó đều sẽ được shutdown và biến quản lý file cũng tự động được đóng sau khi nội dung trong câu lệnh đươc thực thi xong.

## Đọc từ URL

Đọc từ URL cũng giống như đọc từ file, chỉ khác là dùng hàm `urlopen` trong module `request` của package built-in `urllib`

```python
from urllib import request

with request.urlopen('https://google.com') as h:
    print(h.read())
```

## Bài tập

Làm lại các bài tập sau của chương 3

1. Cho một list/tuple số nguyên `a`, viết hàm in ra các giá trị chẵn của `a`.
2. Cho một list/tuple số nguyên `a`, viết hàm tính tổng các số lẻ của `a`.
3. Cho một list/tuple số nguyên `a` và số nguyên `n`, viết hàm đến số lần xuất hiện của `n` trong `a`.
4. Cho một list/tuple số nguyên `a`, viết hàm đếm số lượng số nguyên tố trong `a`.

Trong đó, việc khai báo list/tuple được quy định trong một file input và kết quả được ghi ra một file output.

Nâng cao:
- Sử dụng một file input duy nhất, giống với file `chap_04/input.txt`. Dòng đầu tiên là số `n`, mỗi dòng tiếp theo là một list/tupple, mỗi số là một phần tử được phân cách bởi dấu phẩy hoặc khoảng trắng.
- Sử dụng một file output duy nhất với định dạng sau:

    ```
    <input>
        <function name 1>: <output 1>
        <function name 2>: <output 2>
    ```

    Ví dụ:

    ```
    1,2,3 4 5 6,7,8
        find_even: 2,4,6,8
        sum_odd: 16
    ```