import tkinter as tk
from tkinter import ttk, messagebox

import psutil
import platform
import time

class SystemInfoModule:
    def __init__(self, parent_notebook, root_app):
        self.parent_notebook = parent_notebook
        self.root_app = root_app
        self.frame = ttk.Frame(parent_notebook)
        self.create_widgets()

    def create_widgets(self):
        # Khởi tạo các widget cho tab "Thông tin hệ thống"
        # Ví dụ: self.system_tree, self.cpu_progress, self.cpu_label, v.v.

        pass

    def update_info(self):
        """Cập nhật thông tin hệ thống và tài nguyên."""
        # Logic để lấy và hiển thị thông tin hệ thống và tài nguyên
        # Ví dụ: dùng psutil.cpu_percent(), platform.system(), v.v.
        try:
            # ... code lấy và cập nhật dữ liệu ...
            pass
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể cập nhật thông tin hệ thống: {str(e)}")

    def start_periodic_update(self):
        """Bắt đầu cập nhật thông tin hệ thống định kỳ."""
        self.update_info()  # Cập nhật lần đầu ngay lập tức
        self.root_app.after(5000, self._periodic_update_callback)  # Lên lịch cho lần tiếp theo

    def _periodic_update_callback(self):
        """Callback cho việc cập nhật định kỳ."""
        self.update_info()
        self.root_app.after(5000, self._periodic_update_callback)  # Tiếp tục lên lịch