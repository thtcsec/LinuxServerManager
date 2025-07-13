import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog


def human_readable(size, decimal_places=1):
    """Chuyển đổi byte -> dạng KB/MB/GB… dễ đọc."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.{decimal_places}f} {unit}"
        size /= 1024
    return f"{size:.{decimal_places}f} PB"


class FileBrowser:
    def __init__(self, parent_notebook):
        self.frame = ttk.Frame(parent_notebook)
        self.current_path = tk.StringVar(value=os.path.expanduser('~'))
        self.create_widgets()
        self.refresh_files()

    def create_widgets(self):
        # thanh điều khiển
        control_frame = ttk.Frame(self.frame)
        control_frame.pack(fill='x', padx=5, pady=5)

        path_entry = ttk.Entry(control_frame, textvariable=self.current_path, width=80)
        path_entry.pack(side='left', fill='x', expand=True)

        browse_btn = ttk.Button(control_frame, text="Duyệt", command=self.browse_directory)
        browse_btn.pack(side='left', padx=5)

        refresh_btn = ttk.Button(control_frame, text="Làm mới", command=self.refresh_files)
        refresh_btn.pack(side='left', padx=5)

        # treeview
        columns = ("name", "size", "type")
        self.tree = ttk.Treeview(self.frame, columns=columns, show='headings')
        self.tree.heading("name", text="Tên")
        self.tree.heading("size", text="Kích thước")
        self.tree.heading("type", text="Loại")

        self.tree.column("name", width=300)
        self.tree.column("size", width=100, anchor='e')
        self.tree.column("type", width=100)

        self.tree.pack(fill='both', expand=True, padx=5, pady=5)
        self.tree.bind("<Double-1>", self.on_file_double_click)

    def refresh_files(self):
        path = self.current_path.get()
        self.tree.delete(*self.tree.get_children())
        try:
            if os.path.isdir(path):
                if os.path.dirname(path) != path:
                    self.tree.insert('', 'end', values=('..', '', 'Thư mục'))
                for name in sorted(os.listdir(path)):
                    full_path = os.path.join(path, name)
                    if os.path.isdir(full_path):
                        ftype = 'Thư mục'
                        fsize = '-'
                    else:
                        ftype = 'Tập tin'
                        size_in_bytes = os.path.getsize(full_path)
                        fsize = human_readable(size_in_bytes)
                    self.tree.insert('', 'end', values=(name, fsize, ftype))
            else:
                messagebox.showerror("Lỗi", f"{path} không phải thư mục hợp lệ.")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def browse_directory(self):
        path = filedialog.askdirectory()
        if path:
            self.current_path.set(path)
            self.refresh_files()

    def on_file_double_click(self, event):
        item = self.tree.selection()
        if not item:
            return
        name = self.tree.item(item[0])['values'][0]
        if name == '..':
            self.current_path.set(os.path.dirname(self.current_path.get()))
        else:
            next_path = os.path.join(self.current_path.get(), name)
            if os.path.isdir(next_path):
                self.current_path.set(next_path)
        self.refresh_files()