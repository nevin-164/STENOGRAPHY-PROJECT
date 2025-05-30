import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from cryptography.fernet import Fernet
import os

def load_key():
    if not os.path.exists("secret.key"):
        return None
    with open("secret.key", "rb") as f:
        return f.read()

def from_binary(data):
    chars = []
    for i in range(0, len(data), 8):
        byte = data[i:i+8]
        chars.append(chr(int(byte, 2)))
    return ''.join(chars).split("$$$")[0]

def decode_image(img_path, key):
    img = Image.open(img_path)
    binary_data = ""
    for y in range(img.height):
        for x in range(img.width):
            r, g, b = img.getpixel((x, y))
            binary_data += str(r & 1)

    encrypted = from_binary(binary_data)
    try:
        fernet = Fernet(key)
        return fernet.decrypt(encrypted.encode()).decode()
    except Exception as e:
        return "❌ Decryption failed."

def browse_image():
    path = filedialog.askopenfilename(filetypes=[("PNG Images", "*.png")])
    entry_image.delete(0, tk.END)
    entry_image.insert(0, path)

def decode_action():
    path = entry_image.get()
    if not path or not os.path.isfile(path):
        messagebox.showerror("Error", "Select a valid PNG image.")
        return

    key = load_key()
    if not key:
        messagebox.showerror("Error", "'secret.key' not found.")
        return

    message = decode_image(path, key)
    messagebox.showinfo("🔓 Decoded Message", message)

app = tk.Tk()
app.title("🔍 Decode Message from Image")
app.geometry("500x300")

tk.Label(app, text="🖼️ Select Encoded PNG Image:").pack(pady=10)
entry_image = tk.Entry(app, width=55)
entry_image.pack()
tk.Button(app, text="Browse", command=browse_image).pack(pady=5)

tk.Button(app, text="🔓 Decode Message", command=decode_action).pack(pady=30)
app.mainloop()
