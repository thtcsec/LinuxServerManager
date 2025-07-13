import psutil
import tkinter as tk
from tkinter import ttk, messagebox

class ProcessManager:
    def __init__(self, parent_notebook):
        self.frame = ttk.Frame(parent_notebook)
        self.create_widgets()
        self.refresh_processes()

    def create_widgets(self):
        control_frame = ttk.Frame(self.frame)
        control_frame.pack(fill='x', padx=5, pady=5)

        refresh_btn = ttk.Button(control_frame, text="Làm mới", command=self.refresh_processes)
        refresh_btn.pack(side='left')

        kill_btn = ttk.Button(control_frame, text="Kết thúc Tiến trình", command=self.kill_selected_process)
        kill_btn.pack(side='left', padx=5)

        # Treeview để hiển thị tiến trình
        columns = ("pid", "name", "status", "cpu", "memory")
        self.tree = ttk.Treeview(self.frame, columns=columns, show='headings')
        self.tree.heading("pid", text="PID")
        self.tree.heading("name", text="Tên")
        self.tree.heading("status", text="Trạng thái")
        self.tree.heading("cpu", text="CPU %")
        self.tree.heading("memory", text="Memory %")

        # Định dạng cột
        self.tree.column("pid", width=60, anchor='center')
        self.tree.column("name", width=300)
        self.tree.column("status", width=100)
        self.tree.column("cpu", width=80, anchor='e')
        self.tree.column("memory", width=80, anchor='e')

        self.tree.pack(fill='both', expand=True, padx=5, pady=5)

    def refresh_processes(self):
        self.tree.delete(*self.tree.get_children())
        for proc in psutil.process_iter(['pid', 'name', 'status', 'cpu_percent', 'memory_percent']):
            try:
                # Lấy thông tin, làm tròn số cho dễ nhìn
                pid = proc.info['pid']
                name = proc.info['name']
                status = proc.info['status']
                cpu = f"{proc.info['cpu_percent']:.2f}"
                memory = f"{proc.info['memory_percent']:.2f}"
                self.tree.insert('', 'end', values=(pid, name, status, cpu, memory))
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

    def kill_selected_process(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một tiến trình để kết thúc.")
            return

        item_values = self.tree.item(selected_item[0])['values']
        pid = item_values[0]
        name = item_values[1]

        if messagebox.askyesno("Xác nhận", f"Bạn có chắc chắn muốn kết thúc tiến trình '{name}' (PID: {pid})?"):
            try:
                p = psutil.Process(pid)
                p.terminate() # Hoặc p.kill() nếu muốn mạnh hơn
                messagebox.showinfo("Thành công", f"Đã gửi yêu cầu kết thúc tiến trình '{name}'.")
                self.refresh_processes()
            except psutil.NoSuchProcess:
                messagebox.showerror("Lỗi", "Tiến trình không còn tồn tại.")
            except psutil.AccessDenied:
                messagebox.showerror("Lỗi", "Không có quyền kết thúc tiến trình này.")