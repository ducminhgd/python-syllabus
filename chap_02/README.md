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
