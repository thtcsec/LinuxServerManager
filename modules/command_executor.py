import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import subprocess
import threading

class CommandExecutor:
    def __init__(self, parent_notebook):
        # Frame chứa giao diện của tab
        self.frame = ttk.Frame(parent_notebook)
        self.create_widgets()

    def create_widgets(self):
        # Khung nhập lệnh + nút chạy
        control_frame = ttk.Frame(self.frame)
        control_frame.pack(fill='x', padx=5, pady=5)

        # Entry để người dùng nhập lệnh
        self.command_entry = ttk.Entry(control_frame, width=80)
        self.command_entry.pack(side='left', fill='x', expand=True, padx=5)

        # Nút "Chạy"
        btn_execute = ttk.Button(control_frame, text="Chạy", command=self.run_command_thread)
        btn_execute.pack(side='left')

        # Vùng hiển thị kết quả
        self.output_area = scrolledtext.ScrolledText(self.frame, wrap='word')
        self.output_area.pack(fill='both', expand=True, padx=5, pady=5)

    def run_command_thread(self):
        """Chạy lệnh ở một thread để không block giao diện"""
        cmd = self.command_entry.get()
        if not cmd:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập lệnh.")
            return
        # Tạo thread chạy lệnh
        threading.Thread(target=self.execute_command, args=(cmd,), daemon=True).start()

    def execute_command(self, cmd):
        """Thực thi lệnh bằng subprocess và ghi kết quả ra output_area"""
        self.output_area.insert(tk.END, f"\n$ {cmd}\n")
        self.output_area.see(tk.END)
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            output = result.stdout or ''
            error = result.stderr or ''
            rc = result.returncode

            # Hiển thị stdout
            self.output_area.insert(tk.END, output)
            # Hiển thị stderr
            if error:
                self.output_area.insert(tk.END, error)
            # Hiển thị mã thoát
            self.output_area.insert(tk.END, f"\n[Exit code: {rc}]\n")
            self.output_area.see(tk.END)
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))