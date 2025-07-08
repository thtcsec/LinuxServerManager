import os
import tkinter as tk
from tkinter import ttk, messagebox

# Import các module đã tách
from modules.system_info_module import SystemInfoModule
from modules.process_manager_module import ProcessManagerModule
from modules.network_monitor_module import NetworkMonitorModule
from modules.file_browser_module import FileBrowserModule
from modules.log_viewer_module import LogViewerModule
from modules.command_executor_module import CommandExecutorModule


class LinuxServerManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Linux Server Manager - v1.0")
        self.root.geometry("1200x800")
        self.root.configure(bg='#f0f0f0')

        self.style = ttk.Style()
        self.style.theme_use('clam')

        self.create_menu()

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)

        # Khởi tạo và thêm các tab/module
        # Truyền root_app (self.root) cho SystemInfoModule để nó có thể dùng root.after()
        self.system_info_module = SystemInfoModule(self.notebook, self.root)
        self.notebook.add(self.system_info_module.frame, text="Thông tin hệ thống")

        self.process_manager_module = ProcessManagerModule(self.notebook)
        self.notebook.add(self.process_manager_module.frame, text="Quản lý tiến trình")

        self.network_monitor_module = NetworkMonitorModule(self.notebook)
        self.notebook.add(self.network_monitor_module.frame, text="Mạng")

        self.file_browser_module = FileBrowserModule(self.notebook)
        self.notebook.add(self.file_browser_module.frame, text="Quản lý file")

        self.log_viewer_module = LogViewerModule(self.notebook)
        self.notebook.add(self.log_viewer_module.frame, text="Xem log")

        self.command_executor_module = CommandExecutorModule(self.notebook)
        self.notebook.add(self.command_executor_module.frame, text="Thực thi lệnh")

        # Bắt đầu cập nhật dữ liệu định kỳ cho module thông tin hệ thống
        self.system_info_module.start_periodic_update()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Làm mới tất cả", command=self.refresh_all_modules)
        file_menu.add_separator()
        file_menu.add_command(label="Thoát", command=self.root.quit)

        tools_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Tools", menu=tools_menu)
        tools_menu.add_command(label="Kiểm tra cập nhật", command=self.check_updates)
        tools_menu.add_command(label="Backup hệ thống", command=self.backup_system)

        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="Hướng dẫn", command=self.show_help)
        help_menu.add_command(label="Về chúng tôi", command=self.show_about)

    def refresh_all_modules(self):
        """Làm mới dữ liệu của tất cả các module."""
        self.system_info_module.update_info()
        self.process_manager_module.refresh_processes()
        self.network_monitor_module.refresh_network()
        self.file_browser_module.refresh_files()
        self.log_viewer_module.refresh_log()
        messagebox.showinfo("Làm mới", "Đã làm mới dữ liệu của tất cả các tab.")

    def check_updates(self):
        messagebox.showinfo("Cập nhật", "Tính năng kiểm tra cập nhật sẽ được phát triển trong phiên bản tới.")

    def backup_system(self):
        messagebox.showinfo("Backup", "Tính năng backup hệ thống sẽ được phát triển trong phiên bản tới.")

    def show_help(self):
        help_text = """
        HƯỚNG DẪN SỬ DỤNG ỨNG DỤNG LINUX SERVER MANAGER:

        1. Thông tin hệ thống: Xem thông tin chi tiết về hệ thống và tài nguyên (CPU, RAM, Disk).
        2. Quản lý tiến trình: Xem danh sách các tiến trình đang chạy và kết thúc một tiến trình.
        3. Mạng: Xem thông tin các giao diện mạng, thống kê lưu lượng và thực hiện ping test.
        4. Quản lý file: Duyệt file và thư mục, xem thông tin cơ bản.
        5. Xem log: Chọn và xem 100 dòng cuối của file log.
        6. Thực thi lệnh: Nhập và chạy các lệnh Linux, xem kết quả.

        Lưu ý: Một số tính năng có thể yêu cầu quyền quản trị (sudo).
        """
        messagebox.showinfo("Hướng dẫn", help_text)

    def show_about(self):
        about_text = """
        Linux Server Manager
        Phiên bản: 1.0

        Ứng dụng quản trị cơ bản cho hệ điều hành Linux.
        Được phát triển bằng Python và Tkinter.
        Mã nguồn mở - Tác giả: [Tên của bạn]
        """
        messagebox.showinfo("Về chúng tôi", about_text)


def main():
    root = tk.Tk()
    app = LinuxServerManager(root)
    root.mainloop()


if __name__ == "__main__":
    main()