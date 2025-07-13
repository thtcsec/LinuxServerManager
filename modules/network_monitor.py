# file: network_monitor.py
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, simpledialog
import subprocess
import psutil
import threading

from modules.file_browser import human_readable


class NetworkMonitor:
    def __init__(self, parent_notebook):
        self.parent_notebook = parent_notebook
        self.frame = ttk.Frame(parent_notebook)
        self.create_widgets()
        self.refresh_network()

    def create_widgets(self):
        # Khởi tạo các widget cho tab "Mạng"
        control_frame = ttk.Frame(self.frame)
        control_frame.pack(fill='x', padx=5, pady=5)

        refresh_btn = ttk.Button(control_frame, text="Làm mới", command=self.refresh_network)
        refresh_btn.pack(side='left')

        ping_btn = ttk.Button(control_frame, text="Kiểm tra Ping", command=self.ping_test_dialog)
        ping_btn.pack(side='left', padx=5)

        # Dùng ScrolledText để hiển thị kết quả và có thanh cuộn
        self.network_text = scrolledtext.ScrolledText(self.frame, wrap='word', font=("Courier New", 10))
        self.network_text.pack(fill='both', expand=True, padx=5, pady=5)
        self.network_text.config(state='disabled')

    def _update_text_content(self, content):
        """Hàm an toàn để cập nhật widget Text từ các luồng khác nhau."""
        self.network_text.config(state='normal')
        self.network_text.delete('1.0', tk.END)
        self.network_text.insert(tk.END, content)
        self.network_text.config(state='disabled')

    def refresh_network(self):
        """Cập nhật thông tin mạng."""
        try:
            addrs = psutil.net_if_addrs()
            stats = psutil.net_io_counters(pernic=True)
            content = "--- NETWORK INTERFACES INFO ---\n\n"

            for name, addresses in addrs.items():
                content += f"Giao diện: {name}\n"
                for addr in addresses:
                    if addr.family == psutil.AF_LINK:
                        content += f"  - Địa chỉ MAC : {addr.address}\n"
                    elif addr.family == 2:  # socket.AF_INET (IPv4)
                        content += f"  - Địa chỉ IPv4: {addr.address}\n"
                        content += f"  - Netmask     : {addr.netmask}\n"
                if name in stats:
                    io = stats[name]
                    content += f"  - Đã gửi      : {human_readable(io.bytes_sent)}\n"
                    content += f"  - Đã nhận      : {human_readable(io.bytes_recv)}\n"
                content += "-" * 40 + "\n"

            self._update_text_content(content)

        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể tải thông tin mạng: {str(e)}")

    def ping_test_dialog(self):

            ping_thread = threading.Thread(target=self._run_ping_test, args=("google.com",), daemon=True)
            ping_thread.start()

    def _run_ping_test(self, host):
        """Thực hiện ping test trong một luồng riêng."""
        # Hiển thị thông báo đang ping
        self.frame.after(0, self._update_text_content, f"Đang ping đến {host}...\nVui lòng chờ.")

        try:
            # Lệnh ping cho Linux, gửi 4 gói tin
            command = ["ping", "-c", "4", host]
            result = subprocess.run(command, capture_output=True, text=True, timeout=10)

            output = f"--- KẾT QUẢ PING ĐẾN {host} ---\n\n"
            if result.returncode == 0:
                output += result.stdout
            else:
                output += f"Lỗi: Không thể ping đến {host}.\n"
                output += result.stderr

        except FileNotFoundError:
            output = "Lỗi: Lệnh 'ping' không tồn tại. Hãy chắc chắn bạn đang dùng Linux."
        except subprocess.TimeoutExpired:
            output = f"Lỗi: Ping đến {host} vượt quá thời gian chờ (10 giây)."
        except Exception as e:
            output = f"Đã xảy ra lỗi không xác định: {str(e)}"

        # Cập nhật kết quả lên GUI một cách an toàn
        self.frame.after(0, self._update_text_content, output)