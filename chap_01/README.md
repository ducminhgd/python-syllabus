# Chương 1

## Cài đặt python

1. Windows:
- Download file phù hợp và cài đặt https://www.python.org/downloads/windows/
- Hoặc có thể cài đặt qua Windows Subsystem Linux, sau đó thì sử dụng như trên Linux.
2. Linux:
- Debian (Ubuntu): `sudo apt-get install python3`. Đa số trên các hệ điều hành Debian đều sử dụng Python 2 là mặc định, do đó nếu muốn dùng Python 3 là mặc định thì chạy câu lệnh `sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 1`
- RHEL:
    ```bash
    sudo yum install gcc openssl-devel bzip2-devel libffi-devel
    cd /opt
    wget https://www.python.org/ftp/python/3.8.7/Python-3.8.7.tgz
    tar xzf Python-3.8.7.tgz
    cd Python-3.8.7
    sudo ./configure --enable-optimizations
    sudo make altinstall
    sudo rm Python-3.8.7.tgz
    ```

## Môi trường ảo `virtualenv`

Tùy vào mỗi dự án mà cần dùng những thư viện khác nhau hoặc cùng thư viện nhưng khác phiên bản, để tránh việc xung đột này thì mỗi dự án nên cài đặt môi trường riêng.

1. Cài đặt `virtualenv`
    ```bash
    pip install virtualenv
    ```
1. Tạo môi trường ảo
    ```bash
    cd my_project
    virtualenv .venv
    ```

Đối với Python 3.9 trở về sau thì không cần cài đặt `virtualenv` nữa mà sử dụng `venv` đã có sẵn trong Python 3.9.

    ```bash
    python -m venv .venv
    ```

Câu lệnh trên có ý nghĩa là tại một môi trường ảo với thư mục chứa nó là `my_project/.venv`. Trong trường hợp muốn chỉ định rõ phiên bản python được cài thì sử dụng thêm tùy chọn `-p`, ví dụ: `virtualenv .venv -p python3.8`, hoặc `virtualenv .venv -p python3.9`.

Có 2 cách sử dụng môi trường ảo nếu chạy terminal:
1. Gọi đường dẫn đến file `python` hoặc `pip` cần dùng, ví dụ: `.venv/bin/python`, `.venv/bin/pip`
1. Activate môi trường ảo `source .venv/bin/activate`, khi không dùng nữa có thể gõ lệnh `deactivate`

## Cài đặt packages

Các package nên được khai báo trong file `requirements.txt`.

```
# requirements.txt
pytest
autopep8==1.5.4
pylint~=2.6
# pylint>1,<3
```

Trong đó:

| Điều kiện  |                                            Diễn giải                                            |
| ---------- | ----------------------------------------------------------------------------------------------- |
| Không dùng | Lấy version mới nhất                                                                            |
| `==`       | Lấy đúng version được chỉ định                                                                  |
| `~=`       | Lấy theo version patch mới nhất, ví dụ `pylint` có `2.6.0`, `2.6.1`, `2.6.2` thì sẽ lấy `2.6.2` |
| `<`        | Lấy version mới nhất & nhỏ hơn version được chỉ định                                            |
| `<=`       | Lấy version mới nhất & nhỏ hơn hoặc bằng version được chỉ định                                  |
| `>`        | Lấy version mới nhất & lớn hơn version được chỉ định                                            |
| `>=`       | Lấy version mới nhất & lớn hơn hoặc bằng version được chỉ định                                  |

Có thể kết hợp nhiều điều kiện cùng lúc, ví dụ `pylint>1,<3` là cài đặt version lớn hơn 1 và nhỏ hơn 3, cụ thể lúc viết bài này thì version mới nhất là `2.6.0`, phù hợp với điều kiện trên. 

## Bài tập

1. Cài đặt: Visual Studio Code, Python 3.10, git.
1. Chạy lệnh python và in ra màn hình là `This is system python`, thoát khỏi Python Interpreter.
1. Cài đặt môi trường ảo với thư mục là `.venv`.
1. Chạy IDLE của python của môi trường ảo bằng 2 cách: activate môi trường ảo và trỏ trực tiếp file python của môi trường ảo.