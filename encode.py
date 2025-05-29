from PIL import Image
from cryptography.fernet import Fernet
import os

def generate_key():
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as f:
            f.write(key)
        print("🔐 Key generated and saved to secret.key")
    else:
        print("✅ Key already exists.")
    with open("secret.key", "rb") as f:
        return f.read()

def encode_text_in_image(image_path, message, key, output_path):
    cipher = Fernet(key)
    encrypted_message = cipher.encrypt(message.encode()).decode() + "$$$"
    binary_message = ''.join(format(ord(i), '08b') for i in encrypted_message)

    img = Image.open(image_path)
    encoded = img.copy()
    width, height = img.size
    index = 0

    for row in range(height):
        for col in range(width):
            if index < len(binary_message):
                r, g, b = img.getpixel((col, row))
                r = (r & ~1) | int(binary_message[index])
                encoded.putpixel((col, row), (r, g, b))
                index += 1

    encoded.save(output_path)
    print(f"✅ Message successfully encoded into {output_path}")

if __name__ == "__main__":
    key = generate_key()
    image_path = "input.png"
    output_path = "encoded.png"
    message = input("📝 Enter the message to hide: ")

    if not os.path.exists(image_path):
        print("❌ input.png not found! Place a PNG image in the folder.")
    else:
        encode_text_in_image(image_path, message, key, output_path)

