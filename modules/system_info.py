# file: system_info.py
import tkinter as tk
from tkinter import ttk, messagebox
import psutil
import platform
import time

def human_readable(size, decimal_places=1):
    """Chuyển đổi byte -> dạng KB/MB/GB… dễ đọc."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.{decimal_places}f} {unit}"
        size /= 1024
    return f"{size:.{decimal_places}f} PB"

class SystemDataUtility:
    """Lớp tiện ích để lấy dữ liệu hệ thống THÔ."""
    def get_os_info(self):
        """Trả về thông tin hệ điều hành dưới dạng dictionary."""
        return {
            'OS': platform.system(),
            'OS Release': platform.release(),
            'OS Version': platform.version(),
            'Architecture': platform.machine(),
            'Processor': platform.processor(),
            'Hostname': platform.node(),
            'Python Version': platform.python_version()
        }

    def get_cpu_usage(self):
        """Trả về phần trăm sử dụng CPU (float)."""
        return psutil.cpu_percent(interval=None)

    def get_ram_usage(self):
        """Trả về thông tin RAM dưới dạng dictionary."""
        memory = psutil.virtual_memory()
        return {
            'total': memory.total,
            'used': memory.used,
            'percent': memory.percent
        }

    def get_disk_usage(self, path='/'):
        """Trả về thông tin sử dụng ổ đĩa dưới dạng dictionary."""
        disk = psutil.disk_usage(path)
        return {
            'total': disk.total,
            'used': disk.used,
            'percent': disk.percent
        }

class SystemInfo:
    def __init__(self, parent_notebook, root_app):
        self.parent_notebook = parent_notebook
        self.root_app = root_app # Cần root_app để dùng phương thức 'after'
        self.frame = ttk.Frame(parent_notebook)
        self.data_utility = SystemDataUtility()
        self.create_widgets()
        self.start_periodic_update()

    def create_widgets(self):
        # Khởi tạo các widget cho tab
        # Ghi chú: self.system_tree
        # self.cpu_progress, self.cpu_label
        # self.ram_progress, self.ram_label
        # self.disk_progress, self.disk_label

        main_frame = ttk.Frame(self.frame)
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)

        left_frame = ttk.LabelFrame(main_frame, text="Thông tin cơ bản", padding=10)
        left_frame.pack(side='left', fill='both', expand=True, padx=(0, 5))

        self.system_tree = ttk.Treeview(left_frame, columns=('value',), show='tree headings')
        self.system_tree.heading('#0', text='Thuộc tính')
        self.system_tree.heading('value', text='Giá trị')
        self.system_tree.column('value', width=250)
        self.system_tree.pack(fill='both', expand=True)

        right_frame = ttk.LabelFrame(main_frame, text="Tài nguyên hệ thống", padding=10)
        right_frame.pack(side='right', fill='both', expand=True, padx=(5, 0))

        ttk.Label(right_frame, text="CPU Usage:").pack(anchor='w')
        self.cpu_progress = ttk.Progressbar(right_frame, length=300, mode='determinate')
        self.cpu_progress.pack(fill='x', pady=5)
        self.cpu_label = ttk.Label(right_frame, text="0%")
        self.cpu_label.pack(anchor='w')

        ttk.Label(right_frame, text="RAM Usage:").pack(anchor='w', pady=(20, 0))
        self.ram_progress = ttk.Progressbar(right_frame, length=300, mode='determinate')
        self.ram_progress.pack(fill='x', pady=5)
        self.ram_label = ttk.Label(right_frame, text="0%")
        self.ram_label.pack(anchor='w')

        ttk.Label(right_frame, text="Disk Usage (/):").pack(anchor='w', pady=(20, 0))
        self.disk_progress = ttk.Progressbar(right_frame, length=300, mode='determinate')
        self.disk_progress.pack(fill='x', pady=5)
        self.disk_label = ttk.Label(right_frame, text="0%")
        self.disk_label.pack(anchor='w')

        # Nút làm mới này sẽ cập nhật thông tin tĩnh
        ttk.Button(left_frame, text="Làm mới thông tin cơ bản", command=self.update_static_info).pack(pady=10, side='bottom')

    def update_static_info(self):
        """Cập nhật các thông tin tĩnh như OS, phiên bản..."""
        try:
            # Xóa dữ liệu cũ
            for item in self.system_tree.get_children():
                self.system_tree.delete(item)

            # Lấy và hiển thị dữ liệu mới
            os_info = self.data_utility.get_os_info()
            for key, value in os_info.items():
                self.system_tree.insert('', 'end', text=key, values=(value, ))
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể cập nhật thông tin hệ thống: {str(e)}")

    def update_dynamic_info(self):
        """Cập nhật các thông tin động như CPU, RAM..."""
        try:
            # CPU
            cpu_percent = self.data_utility.get_cpu_usage()
            self.cpu_progress['value'] = cpu_percent
            self.cpu_label.config(text=f"{cpu_percent}%")

            # RAM
            ram_info = self.data_utility.get_ram_usage()
            self.ram_progress['value'] = ram_info['percent']
            self.ram_label.config(text=f"{ram_info['percent']}% ({human_readable(ram_info['used'])} / {human_readable(ram_info['total'])})")

            # Disk
            disk_info = self.data_utility.get_disk_usage()
            self.disk_progress['value'] = disk_info['percent']
            self.disk_label.config(text=f"{disk_info['percent']}% ({human_readable(disk_info['used'])} / {human_readable(disk_info['total'])})")

        except Exception as e:
            # Có thể log lỗi ra console thay vì hiển thị messagebox liên tục
            print(f"Lỗi cập nhật tài nguyên: {e}")

    def start_periodic_update(self):
        """Bắt đầu cập nhật thông tin hệ thống định kỳ."""
        self.update_static_info() # Cập nhật thông tin tĩnh 1 lần
        self._periodic_update_callback() # Bắt đầu vòng lặp cập nhật động

    def _periodic_update_callback(self):
        """Callback cho việc cập nhật định kỳ."""
        self.update_dynamic_info()
        self.root_app.after(2000, self._periodic_update_callback) # Cập nhật tài nguyên mỗi 2 giây