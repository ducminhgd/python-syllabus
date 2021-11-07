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
- https://betterprogramming.pub/5-powerful-python-f-strings-use-cases-acfb6070a8dd

## Ngày giờ



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