#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from app import LinuxServerManager

def main():
    root = tk.Tk()
    app = LinuxServerManager(root)
    root.mainloop()

if __name__ == "__main__":
    main()