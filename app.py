import os
import tkinter as tk
from tkinter import ttk, messagebox

from modules.system_info import SystemInfo
from modules.process_manager import ProcessManager
from modules.network_monitor import NetworkMonitor
from modules.file_browser import FileBrowser
from modules.log_viewer import LogViewer
from modules.command_executor import CommandExecutor


class LinuxServerManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Linux Server Manager")
        self.root.geometry("1200x800")

        self.style = ttk.Style()
        self.style.theme_use('clam')

        self.create_menu()

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)

        # Khởi tạo và thêm các tab/module
        # Truyền root_app (self.root) cho SystemInfoModule để ccó thể dùng root.after()
        self.system_info = SystemInfo(self.notebook, self.root)
        self.notebook.add(self.system_info.frame, text="Thông tin hệ thống")

        self.process_manager = ProcessManager(self.notebook)
        self.notebook.add(self.process_manager.frame, text="Quản lý tiến trình")

        self.network_monitor = NetworkMonitor(self.notebook)
        self.notebook.add(self.network_monitor.frame, text="Mạng")

        self.file_browser = FileBrowser(self.notebook)
        self.notebook.add(self.file_browser.frame, text="Quản lý file")

        self.log_viewer = LogViewer(self.notebook)
        self.notebook.add(self.log_viewer.frame, text="Xem log")

        self.command_executor = CommandExecutor(self.notebook)
        self.notebook.add(self.command_executor.frame, text="Thực thi lệnh")

        # Bắt đầu cập nhật dữ liệu định kỳ cho module thông tin hệ thống
        self.system_info.start_periodic_update()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Làm mới", command=self.refresh_all_modules)
        file_menu.add_separator()
        file_menu.add_command(label="Thoát", command=self.root.quit)

        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="Hướng dẫn", command=self.show_help)
        help_menu.add_separator()
        help_menu.add_command(label="Về ứng dụng", command=self.show_about)

    def refresh_all_modules(self):
        self.system_info.update_info()
        self.process_manager.refresh_processes()
        self.network_monitor.refresh_network()
        self.file_browser.refresh_files()
        self.log_viewer.refresh_log()
        messagebox.showinfo("Làm mới", "Đã làm mới dữ liệu của tất cả các tab.")

    def show_help(self):
        help_text = (
            "ỨNG DỤNG LINUX SERVER MANAGER:\n\n"
            "1.Thông tin hệ thống: Xem thông tin chi tiết về hệ thống và tài nguyên (CPU, RAM, Disk).\n"
            "2.Quản lý tiến trình: Xem danh sách các tiến trình đang chạy và kết thúc một tiến trình.\n"
            "3.Mạng: Xem thông tin các giao diện mạng, thống kê lưu lượng và thực hiện ping test.\n"
            "4.Quản lý file: Duyệt file và thư mục, xem thông tin cơ bản.\n"
            "5.Xem log: Chọn và xem 100 dòng cuối của file log.\n"
            "6.Thực thi lệnh: Nhập và chạy các lệnh Linux, xem kết quả.\n"
        )
        messagebox.showinfo("Hướng dẫn", help_text)

    def show_about(self):
        about_text = (
        "Linux Server Manager\n"

        "Ứng dụng quản trị cơ bản cho hệ điều hành Linux.\n"
        "Phát triển bằng Python và Tkinter.\n"
        "Nhóm 21\n"
            "- Trịnh Hoàng Tú – 23DH113972\n"
            "- Trần Minh Thiện – 23DH113375\n"
        )
        messagebox.showinfo("Về ứng dụng", about_text)
