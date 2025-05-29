from PIL import Image

def decode_text_from_image(image_path):
    img = Image.open(image_path)
    width, height = img.size
    binary_data = ""

    for row in range(height):
        for col in range(width):
            r, g, b = img.getpixel((col, row))
            binary_data += str(r & 1)

    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    message = ""
    for byte in all_bytes:
        character = chr(int(byte, 2))
        message += character
        if message[-3:] == "$$$":
            break

    return message[:-3]  # remove end marker


# Test
print("Decoded message:", decode_text_from_image("encoded.png"))
