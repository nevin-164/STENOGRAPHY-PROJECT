from PIL import Image
from cryptography.fernet import Fernet

def decode_text_from_image(image_path, key):
    # 1. Load image
    img = Image.open(image_path)
    width, height = img.size
    binary_data = ""

    # 2. Extract LSBs from red channel
    for row in range(height):
        for col in range(width):
            r, g, b = img.getpixel((col, row))
            binary_data += str(r & 1)

    # 3. Convert binary to characters
    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    encrypted_message = ""
    for byte in all_bytes:
        character = chr(int(byte, 2))
        encrypted_message += character
        if encrypted_message[-3:] == "$$$":
            break

    encrypted_message = encrypted_message[:-3]  # Remove end marker

    # 4. Decrypt using the key
    cipher = Fernet(key)
    try:
        decrypted_message = cipher.decrypt(encrypted_message.encode()).decode()
        return decrypted_message
    except:
        return "❌ Wrong key or message is corrupted."


if __name__ == "__main__":
    # Load the encryption key from file
    with open("secret.key", "rb") as f:
        key = f.read()

    # Input the image file that has hidden message
    encoded_image = "encoded.png"  # Make sure this file exists

    # Decode and print the message
    message = decode_text_from_image(encoded_image, key)
    print("🕵️‍♂️ Decoded Message:", message)
