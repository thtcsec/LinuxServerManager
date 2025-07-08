XÂY DỰNG ỨNG DỤNG QUẢN TRỊ CƠ BẢN CHO LINUX TRÊN MÃ NGUỒN MỞ
Tên đồ án: Linux Server Manager

Nhóm thực hiện: Nhóm 21

Trịnh Hoàng Tú – 23DH113972

Trần Minh Thiện – 23DH113375
##  Cài đặt

Để cài đặt và chạy ứng dụng Linux Server Manager, cần có môi trường Linux với Python 3 đã được cài đặt.

1.  **Clone Repository:**
    Mở Terminal và clone dự án về máy:

    ```bash
    git clone https://github.com/thtcsec/LinuxServerManager.git
    cd LinuxServerManager
    ```

2.  **Cài đặt các thư viện Python cần thiết:**
    Ứng dụng sử dụng một số thư viện Python mà bạn cần cài đặt. Đảm bảo bạn đã cài đặt `pip` (công cụ quản lý gói của Python).

    ```bash
    pip install -r requirements.txt
    ```

3.  **Quyền hạn:**
    Một số chức năng quản trị hệ thống (ví dụ: kết thúc tiến trình của người dùng khác, đọc một số file log hệ thống) yêu cầu quyền root. Do đó, bạn có thể cần chạy ứng dụng với `sudo`.

    **Lưu ý quan trọng:** Chạy các ứng dụng GUI với `sudo` có thể tiềm ẩn rủi ro bảo mật. Hãy thận trọng và chỉ chạy khi cần thiết.

## 🏃 Cách Sử dụng

Để khởi động ứng dụng:

```bash
  sudo python3 app.py
  # Cần quyền root cho các chức năng quản trị đầy đủ
```