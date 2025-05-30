# 🧠 Text Steganography with AES Encryption 🔐

> ✨ This project was implemented as a personal learning exercise to understand **image-based steganography**, **encryption with AES**, and building a **GUI in Python**. The code structure and techniques are based on existing methods and public resources, modified and built upon to deepen my understanding.

---

## 📚 Project Objective

The main goal of this project was to explore **how secret messages can be hidden inside image files using LSB (Least Significant Bit) steganography**, and how to enhance the security using **AES encryption with a user key**. The project was also an opportunity to practice GUI building with `Tkinter`.

---

## 🔍 What I Learned

```markdown
✅ Fundamentals of image manipulation using Pillow (PIL)
✅ LSB (Least Significant Bit) steganography technique
✅ Basics of symmetric encryption using the Fernet module (AES-based)
✅ Working with binary data and encoding
✅ GUI creation with Tkinter
✅ File handling, key generation, and exception handling in Python
```
Install dependencies:
```markdown
pip install Pillow cryptography
```

🔐 How It Works<br>

Encode<br>

1.Select an image.

2.Type your secret message.

3.A key is generated (secret.key) and the message is encrypted.

4.The encrypted message is hidden inside the image using LSB technique.

5.The output image (e.g., encoded_image.png) is saved.<br>

Decode<br>

1.Open the encoded image.

2.Provide the correct key file.

3.The message is extracted and decrypted if the key is valid.
