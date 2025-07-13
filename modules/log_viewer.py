import os
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox


class LogViewer:
    def __init__(self, parent_notebook):
        self.frame = ttk.Frame(parent_notebook)
        parent_notebook.add(self.frame, text="Xem Log")
        self.create_widgets()

    def create_widgets(self):
        control_frame = ttk.Frame(self.frame)
        control_frame.pack(fill='x', padx=5, pady=5)

        ttk.Label(control_frame, text="Chọn file log:").pack(side='left', padx=5)

        # Gợi ý file log trong /var/log/
        self.log_files = self.get_log_files('/var/log/')

        self.log_combobox = ttk.Combobox(
            control_frame,
            values=self.log_files,
            width=50
        )
        if self.log_files:
            self.log_combobox.current(0)
        self.log_combobox.pack(side='left', padx=5)

        ttk.Button(control_frame, text="Xem", command=self.load_log).pack(side='left', padx=5)

        self.log_text = scrolledtext.ScrolledText(self.frame, width=100, height=30)
        self.log_text.pack(fill='both', expand=True, padx=5, pady=5)

    def get_log_files(self, log_dir):
        """
        Lấy danh sách file trong thư mục log_dir.
        Chỉ lấy các file (bỏ qua thư mục con).
        """
        try:
            files = []
            for f in os.listdir(log_dir):
                full_path = os.path.join(log_dir, f)
                if os.path.isfile(full_path):
                    files.append(full_path)
            return sorted(files)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể đọc thư mục log:\n{e}")
            return []

    def load_log(self):
        log_file = self.log_combobox.get()
        if not os.path.exists(log_file):
            messagebox.showerror("Lỗi", f"File không tồn tại: {log_file}")
            return

        try:
            with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
                last_lines = lines[-100:]
                content = ''.join(last_lines)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể đọc file log:\n{e}")
            return

        self.log_text.delete('1.0', tk.END)
        self.log_text.insert(tk.END, content)

