import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as f:
        f.write(key)
    return key

def encrypt_message(message, key):
    fernet = Fernet(key)
    return fernet.encrypt(message.encode()).decode() + "$$$"

def to_binary(msg):
    return ''.join(format(ord(char), '08b') for char in msg)

def encode_image(img_path, message, key):
    encrypted = encrypt_message(message, key)
    binary_msg = to_binary(encrypted)

    img = Image.open(img_path)
    encoded = img.copy()
    w, h = img.size
    idx = 0

    for y in range(h):
        for x in range(w):
            if idx < len(binary_msg):
                r, g, b = img.getpixel((x, y))
                r = (r & ~1) | int(binary_msg[idx])
                encoded.putpixel((x, y), (r, g, b))
                idx += 1

    encoded.save("encoded.png")
    return True

def browse_image():
    path = filedialog.askopenfilename(filetypes=[("PNG Images", "*.png")])
    entry_image.delete(0, tk.END)
    entry_image.insert(0, path)

def encode_action():
    path = entry_image.get()
    message = entry_msg.get("1.0", tk.END).strip()
    if not path or not os.path.isfile(path):
        messagebox.showerror("Error", "Select a valid PNG image.")
        return
    if not message:
        messagebox.showerror("Error", "Enter a secret message.")
        return

    key = generate_key()
    success = encode_image(path, message, key)
    if success:
        messagebox.showinfo("Success", "✅ Message encoded in 'encoded.png'\n🔑 Key saved as 'secret.key'")

app = tk.Tk()
app.title("🧪 Encode Message in Image")
app.geometry("500x400")

tk.Label(app, text="🖼️ Select PNG Image:").pack(pady=10)
entry_image = tk.Entry(app, width=55)
entry_image.pack()
tk.Button(app, text="Browse", command=browse_image).pack(pady=5)

tk.Label(app, text="🔐 Enter Secret Message:").pack(pady=10)
entry_msg = tk.Text(app, height=5, width=60)
entry_msg.pack()

tk.Button(app, text="✅ Encode Message", command=encode_action).pack(pady=20)
app.mainloop()
