ĐỀ TÀI: XÂY DỰNG ỨNG DỤNG QUẢN TRỊ CƠ BẢN CHO LINUX TRÊN MÃ NGUỒN MỞ

Tên đồ án: Linux Server Manager

Nhóm thực hiện: Nhóm 21

Trịnh Hoàng Tú – 23DH113972

Trần Minh Thiện – 23DH113375
## ⚙️ Cài đặt

Để cài đặt và chạy ứng dụng Linux Server Manager, bạn cần có:

- Môi trường hệ điều hành Linux
- Python >= 3.6
- `pip` (trình quản lý gói Python)

### 🔽 Bước 1: Cài đặt Python (nếu chưa có)

#### 📦 Trên Debian/Ubuntu:
```bash
sudo apt update
sudo apt install python3 python3-pip
```
#### 📦 Trên Fedora:
```bash
sudo dnf install python3 python3-pip
```
### 📌 Kiểm tra phiên bản sau khi cài:
```bash
python3 --version
pip3 --version
```
### Bước 2: **Clone Repository:**
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
    Một số chức năng quản trị hệ thống (ví dụ: kết thúc tiến trình của người dùng khác, đọc một số file log hệ thống) yêu cầu quyền root. Do đó, có thể cần chạy ứng dụng với `sudo`.


## 🏃 Cách Sử dụng

Để khởi động ứng dụng:

```bash
  sudo python3 app.py
  # Cần quyền root cho các chức năng quản trị đầy đủ
```
