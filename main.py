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
# def create_playfair_matrix(key_string):
#     alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # I/J gộp
#     key_string = key_string.upper().replace("J", "I")
#
#     seen = set()
#     key_unique = ""
#     for c in key_string:
#         if c in alphabet and c not in seen:
#             seen.add(c)
#             key_unique += c
#
#     for c in alphabet:
#         if c not in seen:
#             key_unique += c
#
#     # Tạo ma trận 4 cột
#     matrix = [list(key_unique[i:i+4]) for i in range(0, len(key_unique), 4)]
#     return matrix
#
# def find_position(matrix, char):
#     for row_idx, row in enumerate(matrix):
#         for col_idx, cell in enumerate(row):
#             if cell == char:
#                 return row_idx, col_idx
#     return None, None
#
# def playfair_decrypt(ciphertext, matrix):
#     ciphertext = ciphertext.upper().replace("J", "I")
#     # Loại bỏ ký tự không hợp lệ
#     ciphertext = ''.join(c for c in ciphertext if c.isalpha())
#
#     # Kiểm tra độ dài chẵn
#     if len(ciphertext) % 2 != 0:
#         raise ValueError("Ciphertext phải có độ dài chẵn để giải mã Playfair.")
#
#     digraphs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
#     plaintext = ""
#
#     for digraph in digraphs:
#         a, b = digraph[0], digraph[1]
#         row_a, col_a = find_position(matrix, a)
#         row_b, col_b = find_position(matrix, b)
#
#         if row_a is None or row_b is None:
#             raise ValueError(f"Ký tự '{a}' hoặc '{b}' không tồn tại trong bảng Playfair.")
#
#         if row_a == row_b:
#             # Cùng hàng
#             plaintext += matrix[row_a][(col_a - 1) % 4]
#             plaintext += matrix[row_b][(col_b - 1) % 4]
#         elif col_a == col_b:
#             # Cùng cột
#             plaintext += matrix[(row_a - 1) % len(matrix)][col_a]
#             plaintext += matrix[(row_b - 1) % len(matrix)][col_b]
#         else:
#             # Hình chữ nhật
#             plaintext += matrix[row_a][col_b]
#             plaintext += matrix[row_b][col_a]
#
#     return plaintext
#
#
# # Dữ liệu đầu vào
# ciphertext_pf = "Kvecoyntvxwyxifnvdtnbyvcdanuvgqggbkfpbqud"
# key_playfair = "Nipoguovdte"
#
# # Tạo bảng và giải mã
# matrix = create_playfair_matrix(key_playfair)
# plaintext_key = playfair_decrypt(ciphertext_pf, matrix)
# print("Khóa AES K sau khi giải Playfair là:\n", plaintext_key)
